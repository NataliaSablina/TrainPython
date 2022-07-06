from math import pi


__default_radius = 5


def circle_area(radius=__default_radius):
    return round(pi*pow(radius, 2), 8)


def circle_perimetr(radius=__default_radius):
    return round(2*pi*radius, 8)
