# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой
import math


def is_circle_inside(x1, y1, x2, y2, r1, r2):
    if r1 > r2:
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) + r2 <= r1
    else:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + r1 <= r2

print(is_circle_inside(100, 100, 200, 200, 100, 200))
print(is_circle_inside(100, 100, 120, 120, 100, 50))
print(is_circle_inside(100, 100, 200, 200, 200, 20))
print(is_circle_inside(100, 100, 100, 100, 100, 200))
