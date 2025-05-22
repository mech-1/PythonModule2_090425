def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            # print(_cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        # print(_cache)
        return result

    return wrapper

@cache
def fibonacci(n):
    """
    Вычисляет n-ое число Фибоначчи.

    Числа Фибоначчи - это последовательность, в которой каждое число является
    суммой двух предыдущих чисел.

    Например:
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """

    # Базовый случай: первые два числа Фибоначчи
    if n <= 1:
        return n
    # Рекурсивный случай: n-ое число Фибоначчи - это сумма двух предыдущих чисел
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования
print(fibonacci(300))  # Вывод: 13