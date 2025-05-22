# Все алгоритмы сортировки из examples/ оберните в функции
def benchmark(iters=1):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'[*] Среднее время выполнения: {total / iters} секунд.')
            return return_value

        return wrapper

    return actual_decorator

def bubble_sort(nums) -> None:
    swapped = True
    last = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - last):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        last += 1


def sort_choice(nums) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


@benchmark(iters=10)
def quick_sort(nums) -> None:
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def partition(nums, low, high):
        # Выбираем средний элемент в качестве опорного
        # Также возможен выбор первого, последнего
        # или произвольного элементов в качестве опорного
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # Если элемент с индексом i (слева от опорного) больше, чем
            # элемент с индексом j (справа от опорного), меняем их местами
            nums[i], nums[j] = nums[j], nums[i]

    def _quick_sort(items, low, high):
        if low < high:
            # Индекс опорного элемента
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


@benchmark(iters=10)
def test_sort(nums):
    nums.sort()

# Напишите функцию для заполнения списка случайными числами
def gen_list(size: int, at: int = -100, to: int = 100) -> list:
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))
    return data

# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков
test_list = gen_list(100_000)
# print(test_list)
# quick_sort(test_list) # 0.32
test_sort(test_list)    # 0.0024
#  n     ???
# 100 - 250 -           2.5 * 100
# 1000 - 3900 -         3.9 * 1000
# 10.000 - 54.300       5.4 * 10.000
# 100.000 - 710.000     7.1 * 100.000
# O(n^2) - bubble sort
# O(n^2) - sort choice
# O(log(n)*n) - quick sort
# print(test_list)