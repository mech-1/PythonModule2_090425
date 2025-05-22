import math

flat_number = int(input("flat:"))

# Вариант-1:
# floor_number = (flat_number - 1) // 5 + 1
# Вариант-2:
floor_number = math.ceil(flat_number / 5)

print("Квартира", flat_number, "находится на", floor_number, "этаже")
print(f"Квартира {flat_number} находится на {floor_number} этаже")

# 1. Анализируете условие задачи
# 2. Составление алгоритма
# 3. Реализуете алгоритм на языке программирования
# 4. Проверяете свое решения