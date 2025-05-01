# Дан словарь и ключ.
# Напишите программу,
# которая удаляет элемент из словаря по ключу. Если ключ отсутствует, ничего не делает.

my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Enter key: ")

# Variant 1
if key in my_dict:
    del my_dict[key]

# Variant 2
# my_dict.pop(key, None)

print(my_dict)
