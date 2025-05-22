# Дана строка.
# Напишите программу, которая подсчитывает частоту каждого символа в строке.

text = "hello world hello python world"

frequency = {}

for char in text:
    if char in frequency: # уже встречали данный символ
        frequency[char] += 1
    else: # символ встречаем первый раз
        frequency[char] = 1

print(frequency)

