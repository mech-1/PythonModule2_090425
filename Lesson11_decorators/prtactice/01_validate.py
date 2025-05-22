# Напишите декоратор validate_arguments, который проверяет,
# что все аргументы декорируемой функции являются положительными числами.
# Если какой-либо аргумент не удовлетворяет этому условию, декоратор должен выводить сообщение об ошибке.


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Все аргументы должны быть > 0")
        return func(*args, **kwargs)

    return wrapper


@validate_arguments
def calculate_sum(a, b):
    return a + b


print(calculate_sum(5, 10))
print(calculate_sum(-1, 5))
