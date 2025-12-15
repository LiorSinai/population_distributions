import numpy as np
from shapely import Polygon, MultiPolygon
from typing import List

# -------------------------------------------#
#                 Ticks
# -------------------------------------------#

def get_number_decimals(x):
    if isinstance(x, int):
        return 0
    return len(str(x).split('.')[1])


def auto_step(x_min: float, x_max:float, num_steps: int=10):
    step_size = abs(x_min - x_max) / num_steps
    step10 = 10 ** np.round(np.log10(step_size))
    return step10


def get_start(x_min: float, x_max: float, step_size: float):
    if x_min < 0.0 and x_max > 0.0:
        # include 0.0 by starting at an integer number of steps away
        start = 0.0 - np.floor(-x_min/step_size) * step_size
    else:
        start = np.round(x_min, decimals=get_number_decimals(step_size))
    while start < x_min:
        start += step_size
    return start


def get_projection_xticks(
        transform, width: int, height:int
        , step_size: float=None, num_steps: int=10
    ): 
    x_min, y_max = transform * (0, 0)
    x_max, y_min = transform * (width, height) 
    if step_size is None:
        step_size = auto_step(x_min, x_max, num_steps=num_steps)
    start = get_start(x_min, x_max, step_size)
    ticklabels = np.arange(start, x_max, step_size)
    ticklabels = np.round(ticklabels, decimals=get_number_decimals(step_size))
    transform_inverse = transform.__invert__()
    ticks = [transform_inverse * (x, 0) for x in ticklabels]
    ticks = [t[0] for t in ticks]
    return ticks, ticklabels


def get_projection_yticks(
        transform, width: int, height:int
        , step_size: float=None, num_steps: int=10
    ):  
    x_min, y_max = transform * (0, 0)
    x_max, y_min = transform * (width, height)
    if step_size is None:
        step_size = auto_step(y_min, y_max, num_steps=num_steps)
    y_start = get_start(y_min, y_max, step_size)
    ticklabels = np.arange(y_start, y_max, step_size)
    ticklabels = np.round(ticklabels, decimals=get_number_decimals(step_size))
    transform_inverse = transform.__invert__()
    ticks = [transform_inverse * (0, y) for y in ticklabels] 
    ticks = [t[1] for t in ticks]
    return ticks, ticklabels


# -------------------------------------------#
#            Plot polygons
# -------------------------------------------#


def plot_polygon(axes, geometry, *args, offset: np.array = np.array([0, 0]), **kwargs):
    if isinstance(geometry, Polygon):
        xs, ys = geometry.exterior.coords.xy
        axes.plot(xs + offset[0], ys + offset[1], *args, **kwargs)
    elif isinstance(geometry, MultiPolygon):
        for polygon in geometry.geoms:
            xs, ys = polygon.exterior.coords.xy
            axes.plot(xs + offset[0], ys + offset[1], *args, **kwargs)
    else:
        raise Exception(f"Shape of type {type(geometry)} is not supported")
    return axes


def plot_polygons(axes, polygons: List, *args, **kwargs):
    for idx, geometry in enumerate(polygons):
        plot_polygon(axes, geometry, *args, **kwargs)
    return axes


def plot_polygon_transform(
    axes, geometry, transform, *args, offset: np.array = np.array([0, 0]), **kwargs
    ):
    if isinstance(geometry, Polygon):
        polygons = [geometry]
    elif isinstance(geometry, MultiPolygon):
        polygons = geometry.geoms
    else:
        raise Exception(f'Geometry of type \'{type(geometry)}\' is not supported')
    for polygon in polygons:
        transformed_poly = [transform * coords + offset for coords in polygon.exterior.coords]
        xs = [coords[0] for coords in transformed_poly]
        ys = [coords[1] for coords in transformed_poly]
        axes.plot(xs, ys, *args, **kwargs)
    return axes


def plot_polygons_transform(
        axes, geometries: List[Polygon],
        transform, *args,
        offset: np.array = np.array([0, 0]),
    **kwargs):
    for geom in geometries:
        plot_polygon_transform(axes, geom, transform, *args, offset=offset, **kwargs)
    return axes
