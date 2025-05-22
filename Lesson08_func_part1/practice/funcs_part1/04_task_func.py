# Задача: Дан список из n элементов, заполненный произвольными целыми числами.
# Найдите сумму всех положительных элементов.

def sum_positive(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number
    return summa

# Решение:

print(sum_positive([2, -6, 4, 12, 0, -10])) # 18
print(sum_positive([5, -6, 4, -12, 8, -10])) # 17

