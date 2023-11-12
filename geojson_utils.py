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

def get_polygons(features, identifier='shapeName', mainland=False):
    shapes = {}
    for idx, feat in enumerate(features):
        geometry_type = feat['geometry']['type']
        id = feat['properties'][identifier]
        if (id in shapes):
            raise Exception('Duplicate id: ' + id)
        if geometry_type== 'Polygon':
            coords = feat['geometry']['coordinates'][0]
            polygon = Polygon(coords)
            shapes[id] = polygon
        elif geometry_type== 'MultiPolygon':
            polygons = []
            areas = []
            for coords in feat['geometry']['coordinates']:
                polygon = Polygon(coords[0])
                polygons.append(polygon)
                areas.append(polygon.area)
            if mainland:
                # assume mainland is the largest area and all others are islands
                idx = np.argmax(areas)
                shapes[id] = polygons[idx]
            else:
                multipolygon = MultiPolygon(polygons)
                shapes[id] = multipolygon
        else:
            print(f'Feature at idx {idx} is of type {geometry_type} is not supported')
    return shapes