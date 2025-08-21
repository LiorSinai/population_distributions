from shapely import Polygon, MultiPolygon, Point
import numpy as np
from typing import List

def filter_features(shape_data: List[dict], prop_name: str, prop_val):
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] == prop_val:
            features.append(feature)
    return features


def filter_features_by_list(shape_data: List[dict], prop_name: str, prop_list: List):
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] in prop_list:
            features.append(feature)
    return features


def filter_features_by_bounds(shape_data: List[dict], boundary: Polygon):
    valid_features =  []
    for idx, feature in enumerate(shape_data['features']):
        geometry = feature['geometry']
        if geometry['type'] == 'Polygon':
            coordinates = geometry['coordinates'][0]
        elif geometry['type'] == 'MultiPolygon':
            coordinates = sum((polygon[0] for polygon in geometry['coordinates']), [])
        else:
            type_ = geometry['type']
            raise Exception(f"Geometry f type {type_} is not supported")
        if all(boundary.contains(Point(*point)) for point in coordinates):
            valid_features.append(feature)
    return valid_features


def convert_dict_to_shapely(geometry: dict, keep_top: int = -1):
    geometry_type = geometry['type']
    if geometry_type == 'Polygon':
        coords = geometry['coordinates']
        holes = coords[1:] if len(coords) > 1 else None
        polygon = Polygon(coords[0], holes=holes)
    elif geometry_type== 'MultiPolygon':
        polygons = []
        for coords in geometry['coordinates']:
            holes = coords[1:] if len(coords) > 1 else None
            polygon = Polygon(coords[0], holes=holes)
            polygons.append(polygon)
        if keep_top > 0:
            areas = [p.area for p in polygons]
            if keep_top == 1:
                idx = np.argmax(areas)
                polygon = polygons[idx]
            else:
                idxs = np.argsort(areas)[:(-keep_top - 1):-1]
                polygon = MultiPolygon([polygons[i] for i in idxs])
        else:
            polygon = MultiPolygon(polygons)
    else:
        raise Exception(f"Type not supported: {geometry_type}")
    return polygon


def get_polygons(features, identifier='shapeName', keep_top: int =-1):
    shapes = {}
    for idx, feat in enumerate(features):
        id = feat['properties'][identifier]
        if (id in shapes):
            raise Exception('Duplicate id: ' + id)
        polygon = convert_dict_to_shapely(feat['geometry'], keep_top=keep_top)
        shapes[id] = polygon
    return shapes
