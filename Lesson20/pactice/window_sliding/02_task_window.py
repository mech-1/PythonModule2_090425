# Дана строка.
# Найти длину самой длинной подстроки без повторяющихся символов.
#
string = "+bcdefgdhjkooqq"

# Алгоритм
# 1. Двигаем end ->, пока все символы уникальные
# 2. Пока есть дубликаты, двигаем start ->
# 3. end добрался до конца строки - конец
start = 0
end = 1

char_set = set(string[start])
max_len = 0
while end < len(string):
    if string[end] not in char_set: # нет дубликатов
        char_set.add(string[end])
        if len(char_set) > max_len:
            max_len = len(char_set)
        end += 1
    else: # нашли дубликат
        char_set.remove(string[start])
        start += 1

print(max_len)