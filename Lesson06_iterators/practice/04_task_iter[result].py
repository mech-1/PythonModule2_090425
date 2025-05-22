text = "мама мылА рАму"
vowels = "ауоыэяюёие"

num_vowels = 0
for letter in text.lower():
    if letter in vowels:
        num_vowels += 1

print(num_vowels)