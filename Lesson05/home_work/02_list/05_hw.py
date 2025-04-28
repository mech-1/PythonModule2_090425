# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
i = 0
longest_index = 0

while i < len(names):
    if len(names[longest_index]) < len(names[i]):
        longest_index = i
    i = i + 1

print(names[longest_index])
