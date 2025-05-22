# import os
from pathlib import Path

summa = 0
# path = os.path.join('data', 'info.txt')
# path_out = os.path.join('data', 'info_out.txt')
path = Path("data") / "info.txt"
path_out = Path("data") / "info_out.txt"
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if line.strip().isnumeric() or (line[0] == '-' and line[1:].strip().isnumeric()):
            summa += int(line)
print(f"Сумма всех чисел = {summa}")
with open(path_out, 'w', encoding='UTF-8') as f:
    f.write(f"Сумма всех чисел = {summa}")
# Уточнение: в сумму добавляем только те значения, которые можно преобразовать к int'у
# Например: int("-26") --> -26, а int("--26") --> ошибка