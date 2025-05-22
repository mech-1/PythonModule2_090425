# Дан список целых чисел и число k.
# Найти максимальную сумму последовательных элементов списка длины k.

data = [3, 2, -5, 12, 4, 8, 6, 20, 7, 0]
k = 2

start = 0
end = k - 1
max_sum = 0

while end < len(data):
    current_sum = sum(data[start: end + 1])
    if current_sum > max_sum:
        max_sum = current_sum

    start += 1
    end += 1

print(max_sum)