import json
from pathlib import Path

# Задача: Прочитайте информацию из файлов json_data01.json ... json_data06.json
# Выведите названия файлов, содержащих некорректный JSON(с ошибками)

path = Path("data")

file_names = ['json_data01.json', 'json_data02.json', 'json_data03.json',
              'json_data04.json', 'json_data05.json', 'json_data06.json']

with open(path / file_names[2], "r") as file:
    try:
        data = json.load(file)
    except json.decoder.JSONDecodeError:
        print("Ошибка в JSON-файле")

# path / file_names[0]
# path / file_names[1]
# path / file_names[2]
#
# {
#   "name": "Петр",
#   "age": 25,
# }