#
n = int(input("Количество карточек: "))
i = 1
full_sum = 0  # Полная сумма всех карточек
while i <= n:
    full_sum += i
    i += 1
# Цикл, который выполнится n-1 раз
current_sum = 0  # сумма, без учета потерянной карточки
i = 1
while i <= n - 1:
    card_number = int(input("Номер карточки: "))
    current_sum += card_number
    i += 1

print("Номер потерянной карточки:", full_sum - current_sum)

# n = 5
# card | 2 | 4 | 5 | 1 |
