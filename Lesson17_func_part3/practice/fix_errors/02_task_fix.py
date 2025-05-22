# Дана функция
def max_value(*args):
    "Нахождение максимального"
    maximum = args[0]
    for arg in args:
        if maximum < arg:
            maximum = arg
    return maximum


assert max_value(2, 4, -4, 5, 8, 12) == 12
assert max_value(2, 4, -4, 5, 3) == 5
assert max_value(0) == 0
assert max_value(6) == 6
assert max_value(-12, -8, -2, -7, -45) == -2
# Протестируйте работу функции.
# Исправьте ошибки.
# Является ли функция чистой?
