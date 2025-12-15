import logging
import numpy as np
import rasterio
import rasterio.mask
from shapely import MultiPolygon, Polygon
from typing import List, Union

logger = logging.getLogger(__name__)


# https://earth-info.nga.mil/index.php?dir=wgs84&action=wgs84
MAJOR_SEMI_AXIS_WGS84 = 6_378_137 # metres
FLATTENING_WGS84 = 1 / 298.257223563
MINOR_SEMI_AXIS_WGS84 = MAJOR_SEMI_AXIS_WGS84 * (1 - FLATTENING_WGS84)
EARTH_AUTHALIC_RADIUS =  6_371_007.2 # metres. Radius of a sphere with same surface area as the WSG-84 Earth spheroid.
EARTH_RADIUS = EARTH_AUTHALIC_RADIUS


# -------------------------------------------#
#      Great circle distance on a sphere
# -------------------------------------------#

def hav(angle: float):
    return (1 - np.cos(angle))/2


def haversine_formula(long1: float, lat1: float, long2: float, lat2: float):
    """
    Haversine formula for the central angle between two points on a sphere.
    Values must be in radians.
    """
    hav_theta = hav(lat2 - lat1) + np.cos(lat1) * np.cos(lat2) * hav(long2 - long1)
    theta = np.arccos(1 - 2 * hav_theta)
    return theta


def calc_great_circle_distance(point1: tuple, point2: tuple, radius: float = EARTH_AUTHALIC_RADIUS):
    """
    Calculate the great circle distance betweeb two points on a sphere.
    Points are in (longitude, latitude) pairs in degrees.
    By default, the radius is 6,371,007 metres and the result is returned in metres.
    """
    theta = haversine_formula(np.deg2rad(point1[0]), np.deg2rad(point1[1]), np.deg2rad(point2[0]), np.deg2rad(point2[1]))
    distance = radius * theta
    return distance


# -------------------------------------------#
#                Area on a sphere
# -------------------------------------------#


def cylindrical_projection(longitudes: List[float], latitudes: List[float]):
    latitudes = np.deg2rad(np.array(latitudes))
    longitudes = np.deg2rad(np.array(longitudes))
    ys = np.sin(latitudes)
    xs = longitudes
    new_poly = Polygon(zip(xs, ys))
    return new_poly


def calc_area(
        longitudes: List[float], latitudes: List[float],
        radius: float = EARTH_RADIUS
    ):
    """
    Calculate the area of an object on the surface of a sphere by projecting it on a cylinder.
    The longitudes and latitudes must be in degrees.
    By default, the radius is 6,371,007 metres and the result is returned in metres^2.
    """
    # https://stackoverflow.com/questions/4681737/how-to-calculate-the-area-of-a-polygon-on-the-earths-surface-using-python
    poly_cylindrical = cylindrical_projection(longitudes, latitudes)
    area = radius * radius * poly_cylindrical.area # metres^2
    return area

# -------------------------------------------#
#            Density calculations
# -------------------------------------------#


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
            area += calc_area(longs, lats, radius=radius) # metres^2
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
    try:
        clipped_img, transform = rasterio.mask.mask(population_data, [polygon], crop=True)
        clipped_img[clipped_img < 0] = 0 
        population_count = clipped_img.sum() 
    except ValueError as e:
        logger.warning(f"{e} Setting population count to 0.")
        population_count = 0
    longs, lats = polygon.exterior.coords.xy
    area = calc_area(longs, lats, radius=radius) # metres^2 
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
        densities[idx] = population_counts[idx] / (areas[idx]/1e6) # convert to km2
    return densities, population_counts, areas


def get_scales(shape, bounding_polygon: Polygon, radius: float = EARTH_RADIUS):
    height, width = shape
    long_min, lat_min, long_max, lat_max = np.array(bounding_polygon.bounds) * np.pi / 180 # rads
    long_scale = (lat_max - lat_min) * radius / height # rads * metres / pixels = metres/pixels
    lat_scale_top = (long_max - long_min) * radius * np.cos(lat_max) / width # metres/pixels
    lat_scale_bottom = (long_max - long_min) * radius * np.cos(lat_min) / width # metres/pixels
    lat_scale = (lat_scale_top + lat_scale_bottom) / 2
    return long_scale, lat_scale
