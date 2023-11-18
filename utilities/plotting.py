import numpy as np

def get_number_decimals(x):
    if isinstance(x, int):
        return 0
    return len(str(x).split('.')[1])

def get_projection_xticks(transform, width, height, step_size=None): 
    x_min, y_max = transform * (0, 0)
    x_max, y_min = transform * (width, height) 
    if step_size is None:
        step_size = auto_step(x_min, x_max)
    start = get_start(x_min, x_max, step_size)
    ticklabels = np.arange(start, x_max, step_size)
    ticklabels = np.round(ticklabels, decimals=get_number_decimals(step_size))
    transform_inverse = transform.__invert__()
    ticks = [transform_inverse * (x, 0) for x in ticklabels]
    ticks = [t[0] for t in ticks]
    return ticks, ticklabels

def get_projection_yticks(transform, width, height, step_size=None): 
    x_min, y_max = transform * (0, 0)
    x_max, y_min = transform * (width, height)
    if step_size is None:
        step_size = auto_step(y_min, y_max)
    y_start = get_start(y_min, y_max, step_size)
    ticklabels = np.arange(y_start, y_max, step_size)
    ticklabels = np.round(ticklabels, decimals=get_number_decimals(step_size))
    transform_inverse = transform.__invert__()
    ticks = [transform_inverse * (0, y) for y in ticklabels] 
    ticks = [t[1] for t in ticks]
    return ticks, ticklabels

def auto_step(x_min, x_max, num_steps=10):
    step_size = abs(x_min - x_max) / num_steps
    step10 = 10 ** np.round(np.log10(step_size))
    return step10

def get_start(x_min, x_max, step_size):
    if x_min < 0.0 and x_max > 0.0:
        # include 0.0 by starting at an integer number of steps away
        start = 0.0 - np.floor(-x_min/step_size) * step_size
    else:
        start = np.round(x_min, decimals=get_number_decimals(step_size))
    while start < x_min:
        start += step_size
    return start