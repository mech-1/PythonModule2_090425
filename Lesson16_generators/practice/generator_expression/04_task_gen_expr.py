# "Буквы верхнего регистра из строки"
# Генераторное выражение, возвращающее все буквы верхнего регистра из заданной строки.

string = "hello world"
result = (char for char in string.upper())

print(list(result))
