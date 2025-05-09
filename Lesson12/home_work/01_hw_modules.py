# "Вычисление площади случайного треугольника"
# Сгенерируйте случайные координаты трех точек на плоскости.
# Используйте модуль math для вычисления длин сторон треугольника.
# Вычислите площадь треугольника, используя формулу Герона.
import math
import random


def distance(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def triangle_square(a, b, c):
    half_perimeter = (a + b + c) / 2
    square = math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
    return square


point_a = [random.randint(1, 100), random.randint(1, 100)]
point_b = [random.randint(1, 100), random.randint(1, 100)]
point_c = [random.randint(1, 100), random.randint(1, 100)]

ab = point_a + point_b
ac = point_a + point_c
bc = point_b + point_c
a = distance(*ab)
b = distance(*ac)
c = distance(*bc)

print(f"Длина сторон = {a}, {b}, {c}")
print(f"Площадь треугольника = {round(triangle_square(a, b, c), 2)}")
