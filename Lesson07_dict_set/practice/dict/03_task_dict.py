# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.

#          0        1        2       3
keys = ['name', 'surname', 'age', 'rate']
#           0       1        2    3
values = ['Петр', 'Первый', 42, 1300]

# Вариант-1
# person = {}
# for i in range(len(keys)):
#     person[keys[i]] = values[i]
#
# print(person)

# Вариант-2

person = dict(zip(keys, values))
print(person)
