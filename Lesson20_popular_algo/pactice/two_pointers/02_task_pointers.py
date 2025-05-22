# Дан отсортированный список целых чисел и число target.
# Найти два числа в списке, сумма которых равна target.
# Если нет пары чисел равных target, найдите пару, сумма которых максимально близка к target.

data = [3, 5, 8, 11, 14, 16, 18, 21]
target = 40

left = 0
right = len(data) - 1

best_left = data[left]
best_right = data[right]

while True:
    if data[left] + data[right] == target:
        print(f"{data[left]}+{data[right]} == {target}")
        break

    if left == right: # решений нет
        print(f"Решения нет, но {best_left} {best_right}")
        break

    if data[left] + data[right] < target:
        left += 1
    else:
        right -= 1

    current_sum = best_left + best_right
    new_sum = data[left] + data[right]

    if abs(target - new_sum) < abs(target - current_sum):
        best_left = data[left]
        best_right = data[right]