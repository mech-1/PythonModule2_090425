# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
# Variant 1
for name in names:
    print(f'{name}', end=", ")

print()
print('-' * 40)

# Variant 2
for i, name in enumerate(names, 1):
    if i != len(names):
        print(f'{name}', end=", ")
    else:
        print(f'{name}')
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
