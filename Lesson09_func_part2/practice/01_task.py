# Напишите функцию, которая принимает список строк и возвращает новый список,
# где каждая строка преобразована в верхний регистр.
def string_to_upper(string):
    return string.upper()

def to_upper(strings):
    return list(map(string_to_upper, strings))

print(to_upper(["hello", "hi", "name"]))

