# "ASCII коды символов строки"
# Генераторное выражение, возвращающее ASCII коды каждого символа в заданной строке.

string = "hello"

iterator = (ord(char) for char in string)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
for code in iterator:
    print(code)