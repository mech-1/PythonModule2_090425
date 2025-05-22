# Задача "Моделирование броска костей"
# Используйте функцию random.randint() для имитации броска двух игральных костей (числа от 1 до 6).
# Выведите на экран результат броска каждой кости и их сумму.
import random

def drop_dice():
    return random.randint(1, 6)

print(drop_dice())
print(drop_dice())