from shapely import Polygon, MultiPolygon
import numpy as np

def filter_features(shape_data, prop_name, prop_val):
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] == prop_val:
            features.append(feature)
    return features


def filter_features_by_list(shape_data, prop_name, prop_list):
    features = []
    for feature in shape_data['features']:
        if feature['properties'][prop_name] in prop_list:
            features.append(feature)
    return features


def convert_dict_to_shapely(geometry: dict, keep_top = -1):
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


def get_polygons(features, identifier='shapeName', keep_top=-1):
    shapes = {}
    for idx, feat in enumerate(features):
        id = feat['properties'][identifier]
        if (id in shapes):
            raise Exception('Duplicate id: ' + id)
        polygon = convert_dict_to_shapely(feat['geometry'], keep_top=keep_top)
        shapes[id] = polygon
    return shapes
