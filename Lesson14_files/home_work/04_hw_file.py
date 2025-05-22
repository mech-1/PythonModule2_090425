import os
from pathlib import Path
from pprint import pprint

path = os.path.join('data', 'fruits.txt')
DIR = "data"
fruits = {}

with open(path, 'r', encoding="UTF-8") as f:
    for line in f:
        fruit_name = line.strip()
        if not fruit_name:
            continue

        first_letter = fruit_name[0]
        x = fruits.setdefault(first_letter, [])
        x.append(fruit_name)
        fruits[first_letter] = x
pprint(fruits)

for first_letter, fruit_names in fruits.items():
    path_out = Path(DIR, "fruits_" + first_letter)
    with open(path_out, "w", encoding="UTF-8") as f:
        for fruit_name in fruit_names:
            f.write(fruit_name + "\n")

# 10000 -> 20000
# Абрикос -> fruit_A
# Груша -> fruit_Г
# Арбуз -> fruit_А

# fruit_files = {
#     "А": open(".../fruits_А", "w", encoding="UTF-8"),
#     "Б": open(".../fruits_Б", "w", encoding="UTF-8"),
# }

path = "data/fruits.txt"
d = list(map(chr,range(ord("А"),ord("Я")+1)))
with open(path, "r", encoding="UTF-8") as f:
    for line in f:
        if line.strip():
            path1 = "data/"+"fruits_" + line[0] + ".txt"
            with open(path1,"a", encoding="UTF-8")as file:
                file.write(line)