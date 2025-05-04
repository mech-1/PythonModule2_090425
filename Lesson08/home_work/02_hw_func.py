# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой
import math


# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def shortest_segment_name(**kwargs):
    i = 0
    for key, point in kwargs.items():
        distance_temp = distance(*point)
        if i == 0:
            shortest_dist = distance_temp
            segment_name = key
            i += 1
        if distance_temp < shortest_dist:
            shortest_dist = distance_temp
            segment_name = key

    return segment_name
