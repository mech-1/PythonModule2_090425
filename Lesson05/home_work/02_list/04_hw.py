# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import math

source_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []

for number in source_list:
    if number > 0:
        new_item = number ** 0.5
        # if new_item - int(new_item) == 0:
        # if new_item % 1 == 0:
        frac, intNum = math.modf(new_item)
        if frac == 0:
            new_list.append(int(new_item))

print(new_list)
