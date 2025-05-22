# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args) -> float:
    # print(args)
    return sum(args)/len(args)


def gen_list(size:int, at:int=-10, to:int=10) -> list[int]:
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)
my_tuple = 5, 7, -4, 10, 8

result = average(*my_list)
print(result)
