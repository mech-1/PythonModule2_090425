# Даны координаты двух точек на плоскости.
# Напишите функцию нахождения расстояния между двумя точками.
import math


def distance(x1=0, y1=0, x2=0, y2=0):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Тестируем функцию
print(distance(2, 4, 2))
print(distance(2, 4))
print(distance(2))
print(distance())
# print(distance(12, 8, 12, -9))
# print(distance(23, 0, 15, 32))
