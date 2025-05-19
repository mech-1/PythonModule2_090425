# Анаграммы*
# Дан список слов. Найти в нем все анаграммы (слова, составленные из одних и тех же букв).
def find_anagrams(words: list) -> list:
    anagrams = []
    i = 0
    while i < len(words) - 1:
        j = i + 1
        while j < len(words):
            if sorted(words[i].lower()) == sorted(words[j].lower()):
                anagrams.append((words[i], words[j]))
            j += 1
        i += 1
    return anagrams


if __name__ == '__main__':
    original_words = ["липа", "пила", "молоко", "соль", "лось", "лосось", "кот", "ток", "насос", "мир", "Сосна", "Рим"]
    print(find_anagrams(original_words))
