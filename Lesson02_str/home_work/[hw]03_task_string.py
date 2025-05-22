# Посчитайте количество согласных букв в данной строке.

#       012345678910
text = "Simple teyy".upper()
letters = "BCDFGHJKLMNPQRSTVWXZ"

index = 0
num_consonants = 0


while index < len(text):
    if text[index] in letters:
        num_consonants += 1
    index += 1

print(num_consonants)