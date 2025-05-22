numbers = [5, 2, 5, 5, 5, 5, 12, 4, 5, 5, 5, 2]
num_to_remove = 5

# while - до какого-то условия
# while True:
#     if num_to_remove in numbers:
#         numbers.remove(num_to_remove)
#     else: # удалены все нужные числа
#         break

# for in - определенное количество раз
for number in numbers.copy():
    if number == num_to_remove:
        numbers.remove(num_to_remove)

print(numbers)