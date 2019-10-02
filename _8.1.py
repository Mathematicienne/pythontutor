from math import (fabs, sqrt)
def distance(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    c = sqrt(fabs(x) * fabs(x) + fabs(y) * fabs(y))
    return c
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))

