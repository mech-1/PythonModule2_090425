# Задача: Подсчитать количество гласных(русских) букв во введенной строке без учета регистра.
# Решение:
# Оформите решение задачи в виде функции

def count_vowels(text: str) -> int:
    vowels = "ауоыэяюёие"
    num_vowels = 0
    for char in text.lower():
        if char in vowels:
            num_vowels += 1
    return num_vowels


assert count_vowels("мамА мыла РамУ") == 6
assert count_vowels("привет, как дела?") == 5
assert count_vowels("произвольный текст") == 5
assert count_vowels("") == 0
assert count_vowels("грпркцц прсккв") == 0
assert count_vowels("аеоуоаииоэ") == 10