import math

def period(l, g):
    if isinstance(l, str) or isinstance(g, str):
        raise TypeError
    if l < 0 or g <= 0:
        raise ValueError
    c = (2*math.pi)*math.sqrt(l / g)
    return c



