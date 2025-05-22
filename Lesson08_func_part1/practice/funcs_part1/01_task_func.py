# Напишите функцию для расчета площади прямоугольника.
#
# Входные данные:
#   w: ширина прямоугольника.
#   h: высота прямоугольника.
# Результат:
#   площадь прямоугольника.

def calculate_rectangle_area(width: int|float, height: int|float) -> int|float:
    return width * height


result = calculate_rectangle_area(10, 20)
print(result)