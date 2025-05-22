# "Простые числа до 100"
# Генераторное выражение, возвращающее все простые числа в диапазоне до 20

def is_prime(n: int) -> bool:
    """
    Проверяет, является ли заданное целое число простым.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

result = (number for number in range(1, 21) if is_prime(number))
print(list(result))