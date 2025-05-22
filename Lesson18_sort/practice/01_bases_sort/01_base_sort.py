# Дан алгоритм сортировки пузырьком
# Раскомментируйте print-ы, изучите вывод в консоли.
# TODO: Вспомнив теорию, оптимизируйте алгоритм сортировки...
nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
last = 0
while swapped:
    swapped = False
    for i in range(len(nums) - 1 - last):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            swapped = True
    last += 1
print("after sort = ", nums)