# Напишите декоратор to_string, который преобразует результат выполнения декорируемой функции в строку.


def to_string(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper

@to_string
def calculate_sum(a, b):
    return a + b

print(type(calculate_sum(5, 10)))
