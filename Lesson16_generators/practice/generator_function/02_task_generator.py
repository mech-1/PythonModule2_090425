# Задача "Генератор обратного отсчета"
# Напишите генераторную функцию countdown(n), которая генерирует числа в обратном порядке от n до 1.

def countdown(n):
    for number in range(n, 0, -1):
        yield number


print(list(countdown(8)))

