def log(text: str, file: str = "log.txt") -> None:
    with open(file, "a", encoding="UTF-8") as f:
        f.write(text + "\n")


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
# Уточнение: функция log() все сообщения должна записывать на отдельных строках
