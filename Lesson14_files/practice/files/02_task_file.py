# Задаем путь к файлу:
path_read = "data/limericks.txt"  # вместо dir подставь название папки с файлом.
path_write = "data/clean_limericks.txt"

# Открываем файл на чтение
file_in = open(path_read, "r", encoding="UTF-8")
file_out = open(path_write, "w", encoding="UTF-8")

# В переменную line считываем строку за стройкой из файла(f)
for line in file_in:
    new_line = line.replace(".", "")
    file_out.write(new_line)

file_in.close()
file_out.close()
