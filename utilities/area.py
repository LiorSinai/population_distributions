from shapely import MultiPolygon, Polygon
import numpy as np
import rasterio
import rasterio.mask
from typing import List, Union


# https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84
MAJOR_SEMI_AXIS_WGS84 = 6_378_137 # metres
FLATTENING_WGS84 = 1 / 298.257223563
MINOR_SEMI_AXIS_WGS84 = MAJOR_SEMI_AXIS_WGS84 * (1 - FLATTENING_WGS84)
EARTH_AUTHALIC_RADIUS =  6_371_007.2 # metres. Radius of a sphere with same surface area as the WSG-84 Earth spheroid.
EARTH_RADIUS = EARTH_AUTHALIC_RADIUS


def cylindrical_projection(latitudes: List[float], longitudes: List[float]):
    latitudes = np.array(latitudes)
    longitudes = np.array(longitudes)
    ys = np.sin(latitudes * np.pi / 180)
    xs = longitudes * np.pi / 180
    new_poly = Polygon(zip(xs, ys))
    return new_poly


# https://stackoverflow.com/questions/4681737/how-to-calculate-the-area-of-a-polygon-on-the-earths-surface-using-python
def calc_area(
        latitudes: List[float], longitudes: List[float],
        radius: float = EARTH_RADIUS
    ):
    poly_cylindrical = cylindrical_projection(latitudes, longitudes)
    area = radius * radius * poly_cylindrical.area # metres^2
    return area


def show_stats(
        population_data: rasterio.io.DatasetReader,
        geometries: List[Union[Polygon, MultiPolygon]],
        radius: float = EARTH_RADIUS
    ):
    clipped_img, transform = rasterio.mask.mask(population_data, geometries, crop=True)
    clipped_img[clipped_img < 0] = 0                                            
    population_count = clipped_img.sum()
    population_max = clipped_img.max()
    area = 0
    for geometry in geometries:
        polygons = geometry.geoms if isinstance(geometry, MultiPolygon) else [geometry]
        for polygon in polygons:
            longs, lats = polygon.exterior.coords.xy
            area += calc_area(lats, longs, radius=radius) # metres^2
    print(f'population: {population_count/1e6:.2f} million')
    print(f'max:        {population_max:.0f} people / pixel')
    print(f'area:       {area/1e6:.2f} km^2')
    density = population_count / (area/1e6)
    print(f'density:    {density:.2f} people/km^2')


def density_per_polygon(
        population_data: rasterio.io.DatasetReader,
        polygon: Polygon,
        radius: float = EARTH_RADIUS
    ):
    clipped_img, transform = rasterio.mask.mask(population_data, [polygon], crop=True)
    clipped_img[clipped_img < 0] = 0 
    population_count = clipped_img.sum() 
    longs, lats = polygon.exterior.coords.xy
    area = calc_area(lats, longs, radius=radius) # metres^2 
    density = population_count / (area/1e6)
    return density, population_count, area


def get_density_per_area(
        population_data: rasterio.io.DatasetReader,
        shapes: List[Union[Polygon, MultiPolygon]],
        radius: float = EARTH_RADIUS
    ):
    n = len(shapes)
    densities = np.zeros(n)
    population_counts = np.zeros(n)
    areas = np.zeros(n)
    for idx, shape in enumerate(shapes):
        if isinstance(shape, Polygon):
            polygons = [shape]
        elif isinstance(shape, MultiPolygon):
            polygons = shape.geoms
        else:
            type_ = type(shape)
            raise Exception(f"type {type_} is not supported")
        areas[idx] = 0.0
        population_counts[idx] = 0.0
        for polygon in polygons:
            density, population_count, area = density_per_polygon(
                population_data, polygon, radius=radius)
            population_counts[idx] += population_count
            areas[idx] += area
        densities[idx] = population_counts[idx] / (areas[idx]/1e6)
    return densities, population_counts, areas


def get_scales(shape, bounding_polygon: Polygon, radius: float = EARTH_RADIUS):
    height, width = shape
    long_min, lat_min, long_max, lat_max = np.array(bounding_polygon.bounds) * np.pi / 180 # rads
    long_scale = (lat_max - lat_min) * radius / height # rads * metres / pixels = metres/pixels
    lat_scale_top = (long_max - long_min) * radius * np.cos(lat_max) / width # metres/pixels
    lat_scale_bottom = (long_max - long_min) * radius * np.cos(lat_min) / width # metres/pixels
    lat_scale = (lat_scale_top + lat_scale_bottom) / 2
    return long_scale, lat_scale
