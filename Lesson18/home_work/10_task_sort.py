# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.
from random import randint, seed

stones = [randint(5, 50) for _ in range(randint(3, 12))]
print('Вес камней в порядке возрастания:',sorted(stones))


# seed(10)
def sum_heaps(stones: list) -> tuple:
    count = 1
    heap1 = []
    heap2 = []
    for i, stone in enumerate(sorted(stones), 1):
        if count < 2:
            heap1.append(stone)
            count += 1
            if count == 2:
                count += 1
        elif count >= 2:
            heap2.append(stone)
            count -= 1
            if count == 1:
                count -= 1

    return sum(heap1), sum(heap2)


def sum_heaps_v2(stones: list) -> tuple:
    swapped = True
    heap1 = []
    heap2 = []
    for i, stone in enumerate(sorted(stones), 1):
        if swapped:
            heap1.append(stone)
        else:
            heap2.append(stone)
        swapped = not swapped

    return sum(heap1), sum(heap2)


def check_sum(sums: tuple)->str:
    sums = sorted(sums)
    if sums[1] / sums[0] >= 2:
        return(f'Вес куч отличаются более чем в 2 раза. {sums} ')
    return sums

if __name__ == '__main__':
    print(f"Первая функция: {check_sum(sum_heaps(stones))}")
    print(f"Вторая функция:{check_sum(sum_heaps_v2(stones))}")
