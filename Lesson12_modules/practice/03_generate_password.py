# Задача "Генерация случайного пароля"
# Создайте строку, содержащую символы разных регистров, цифры и спецсимволы.
# Используйте функцию random.choice() для выбора случайных символов из этой строки.
# Сгенерируйте пароль заданной длины.
import random

def generate_password(password_length: int) -> str:
    password = ""
    for i in range(password_length):
        password += random.choice(
            [chr(i) for i in range(ord('a'), ord('z'))] +
            [chr(i) for i in range(ord('A'), ord('B'))] +
            [chr(i) for i in range(ord('0'), ord('9'))] + ['@', '!', '_']
        )
    return password

assert len(generate_password(5)) == 5
assert len(generate_password(12)) == 12
assert len(generate_password(16)) == 16
assert len(generate_password(22)) == 22
assert len(generate_password(2)) == 2
