from math import (fabs, sqrt)
def distance(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    c = sqrt(fabs(x) * fabs(x) + fabs(y) * fabs(y))
    return c
print(distance(float(input()), float(input()), float(input()), float(input())))

