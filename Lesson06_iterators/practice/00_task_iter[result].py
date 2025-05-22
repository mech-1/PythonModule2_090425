text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer bibendum nisi ut convallis ante"

# найти количество слов, длина которых больше 5
num_longest_words = 0
words = text.split()
for word in words:
    if len(word) > 5:
        num_longest_words += 1

print("Кол-во слов больше 5 символов: ", num_longest_words)
