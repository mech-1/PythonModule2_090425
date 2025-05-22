# Даны функции
def average(numbers: list) -> float:
    "Нахождение среднеарифметического"
    total = sum(numbers)
    return total / len(numbers)


def get_unique_elements(data: list) -> list:
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)

    return unique


if __name__ == "__main__":
    # assert average([3, 3, 3]) == 3.0
    # assert average([0, 2, 0, 2]) == 1.0
    # assert average([5, 5, 5]) == 5.0
    # assert average([10]) == 10.0
    # assert average([5, -5, 6]) == 2.0

    # Протестируйте работу функции.
    # Исправьте ошибки.
    # Является ли функция чистой?
    # print(get_unique_elements([2, 2, 2, 4, 2, 4, 0]))
    assert get_unique_elements([2, 4, 2, 4, 0]) == [2, 4, 0]
    assert get_unique_elements([-2, 4, -2, -2, 6, 6, 6]) == [-2, 4, 6]
    assert get_unique_elements([]) == []
    assert get_unique_elements([4]) == [4]
    assert get_unique_elements(["hello", "hi", "hello"]) == ["hello", "hi"]
    assert get_unique_elements(["hello", (2, 4), 3, (2, 4), 3, 3]) == ["hello", (2, 4), 3]
