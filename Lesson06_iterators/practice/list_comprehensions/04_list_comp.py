# Дан код:
numbers = [1, 2, 3, 4]
pairs = []
for num in numbers:
    pairs.append((num, num ** 2))
print(pairs)

# Перепишите его, используя list comprehensions:

pairs = [(num, num ** 2) for num in numbers]
print(pairs)
