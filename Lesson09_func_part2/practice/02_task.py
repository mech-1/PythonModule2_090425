# Напишите функцию, которая принимает список чисел и возвращает сумму квадратов этих чисел.
def log(original_func):
    def wrapper(*args, **kwargs):
        print(f"Была вызвана функция {original_func.__name__}")
        return original_func(*args, **kwargs)
    return wrapper

@log
def square(number):
    return number ** 2

@log
def sum_of_squares(numbers):
    return sum(map(square, numbers))

print(sum_of_squares([2, -4, 5]))