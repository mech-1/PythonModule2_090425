# Напишите декоратор cache, который кэширует результаты выполнения декорируемой функции.
# Если функция вызывается с теми же аргументами, что и ранее,
# декоратор должен возвращать сохраненный результат, не выполняя функцию заново.

import time

from tmp.demo_fileter import result


def cache(func):
    _cache = {}

    def wrapper(*args, **kwargs):
        key = args, tuple(sorted(kwargs.items()))
        if key in _cache:
            print(_cache)
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        print(_cache)
        return result

    return wrapper


@cache
def expensive_calculation(n):
    time.sleep(2)
    return n * n


print(expensive_calculation(5))
print(expensive_calculation(5))
print(expensive_calculation(n=4, m=10))
print(expensive_calculation(n=3))
print(expensive_calculation(m=10, n=10))
# print(expensive_calculation(4))
