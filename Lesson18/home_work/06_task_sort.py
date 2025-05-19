# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход:дано N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10
prices1 = [2, 1, 10, 50, 11, 5]
prices2 = [2, 1, 10, 50, 12]


def sum_max_prices(prices: list[int]) -> int:
    sorted_prices = []
    prices.sort()
    j = len(prices)
    # half_length = len(prices) // 2 if len(prices) % 2 == 0 else len(prices) // 2 + 1
    half_length = ceil(len(prices) / 2)
    for i in range(half_length):
        j -= 1
        sorted_prices.append(prices[j])
        if i != j:
            sorted_prices.append(prices[i])
    return sum(sorted_prices[x] for x in range(0,len(sorted_prices),2))


if __name__ == '__main__':
    print(sum_max_prices(prices1))
    print(sum_max_prices(prices2))
    assert sum_max_prices(prices1) == 71
    assert sum_max_prices(prices2) == 72
