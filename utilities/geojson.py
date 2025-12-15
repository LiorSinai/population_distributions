import logging
from shapely import Polygon, MultiPolygon, Point
from typing import List, Union
from utilities.area import calc_great_circle_distance, EARTH_AUTHALIC_RADIUS

logger = logging.getLogger(__name__)

#--------------------------------#
#        Filtering
#--------------------------------#


def filter_features(shape_data: List[dict], prop_name: str, prop_val):
    """
    Return features that match a given property. 
    """
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] == prop_val:
            features.append(feature)
    return features


def filter_features_by_list(shape_data: List[dict], prop_name: str, prop_list: List):
    """
    Return features that match at least one value in a list of values for a given property.
    """
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] in prop_list:
            features.append(feature)
    return features


def extract_coordinates(geometry: dict):
    # ignore holes
    if geometry['type'] == 'Polygon':
        coordinates = geometry['coordinates'][0]
    elif geometry['type'] == 'MultiPolygon':
        coordinates = sum((polygon[0] for polygon in geometry['coordinates']), [])
    else:
        shape_type = geometry['type']
        raise Exception(f"Geometry f type {shape_type} is not supported")
    return coordinates


def filter_features_by_bounds(shape_data: List[dict], boundary: Polygon):
    """
    Return features that fit entirely within the boundary.
    """
    valid_features =  []
    for idx, feature in enumerate(shape_data['features']):
        coordinates = extract_coordinates(feature['geometry'])
        if all(boundary.contains(Point(*point)) for point in coordinates):
            valid_features.append(feature)
    return valid_features


def filter_features_by_proximity(
        shape_data: List[dict],
        point: tuple,
        great_circle_distance: float,
        earth_radius: float = EARTH_AUTHALIC_RADIUS,
        ):
    """
    Return features where at least one point falls with in the `great_circle_distance`.
    By default, the radius is 6,371,007 metres.
    """
    valid_features =  []
    for idx, feature in enumerate(shape_data['features']):
        coordinates = extract_coordinates(feature['geometry'])
        for coord in coordinates:
            d = calc_great_circle_distance(coord, point, radius=earth_radius)
            if d <= great_circle_distance:
                valid_features.append(feature)
                break
    return valid_features


def filter_features_by_area(shape_data: List[dict], min_area: float):
    """
    Return 
    """
    pass


#--------------------------------#
#     Shapely <> GeoJson
#--------------------------------#

def convert_dict_to_shapely(geometry: dict, min_area: float = 0.0):
    geometry_type = geometry['type']
    if geometry_type == 'Polygon':
        coords = geometry['coordinates']
        holes = coords[1:] if len(coords) > 1 else None
        polygon = Polygon(coords[0], holes=holes)
    elif geometry_type == 'MultiPolygon':
        polygons = []
        for coords in geometry['coordinates']:
            holes = coords[1:] if len(coords) > 1 else None
            polygon = Polygon(coords[0], holes=holes)
            if min_area > 0.0 and polygon.area < min_area:
                continue
            polygons.append(polygon)
        polygon = MultiPolygon(polygons)
    else:
        raise Exception(f"Type not supported: {geometry_type}")
    return polygon


def get_polygons(features, identifier='shapeName', **kwargs):
    shapes = {}
    for idx, feat in enumerate(features):
        id = feat['properties'][identifier]
        if (id in shapes):
            new_id = f"{id}-{idx}"
            logger.warning(f"Duplicate {identifier} '{id}'. Setting {identifier} to '{new_id}'.")
            id = new_id
            #raise Exception('Duplicate id: ' + id)
        polygon = convert_dict_to_shapely(feat['geometry'], **kwargs)
        shapes[id] = polygon
    return shapes


def convert_shapely_to_geojson_coords(shape: Union[Polygon, MultiPolygon]):
    shape_type = type(shape)
    if shape_type == Polygon:
        coords = [[list(xy) for xy in shape.exterior.coords]]
        for hole in shape.interiors:
            coords.append([list(xy) for xy in hole.coords])
        type_str = 'Polygon'
    elif shape_type == MultiPolygon:
        coords = []
        for polygon in shape.geoms:
            polygon_coords = [[list(xy) for xy in polygon.exterior.coords]]
            for hole in polygon.interiors:
                polygon_coords.append([list(xy) for xy in hole.coords])
            coords.append(polygon_coords)
        type_str = 'MultiPolygon'
    else:
        raise Exception(f"Type '{shape_type}' is not supported.")
    return type_str, coords
