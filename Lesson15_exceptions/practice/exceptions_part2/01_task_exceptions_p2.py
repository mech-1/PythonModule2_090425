def check_age(age):
    # Добавьте проверку, что возраст должен быть положительным числом.
    # Если возраст некорректный, выбросьте исключение ValueError.
    if age < 0:
        raise ValueError("Возраст должен быть положительный")
    return age

try:
    print(check_age(-5))
except ValueError as e:
    print(e)


# for i in [1, 2, 3, 0, 4, 5]:
#     try:
#         print(10/i)
#     except ZeroDivisionError:
#         print("Попытка деления на ноль")