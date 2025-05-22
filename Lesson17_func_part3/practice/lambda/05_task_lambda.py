# Дан готовый код
def is_positive(num):
    return num > 0


mixed_numbers = [-2, 0, 5, -8, 10]
positive_numbers = list(filter(lambda n: n > 0, mixed_numbers))
print(positive_numbers)

# Задача: перепишите код, используя lambda-функцию
