# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу не используя строки

# def palindrome(number):
#     return str(number) == str(number)[::-1]

def palindrome_v2(number):
    reverse_number = 0
    number_copy = number
    while number_copy != 0:
        digit = number_copy % 10
        reverse_number = reverse_number * 10 + digit
        number_copy = number_copy // 10
    return number == reverse_number


# 1234 | "1234"[::-1] -> "4321"

# Тестируем функцию
print(palindrome_v2(1234))
print(palindrome_v2(3443))
print(palindrome_v2(1234541))
print(palindrome_v2(1234321))
print(palindrome_v2(77777))

# Подсказка:
# Самый простой способ решить задачу, работать с полученным числом как со строкой
# Преобразование к строке:  str(1234) --> "1234"
# Переворот строки:         "1234"[::-1] --> "4321"
