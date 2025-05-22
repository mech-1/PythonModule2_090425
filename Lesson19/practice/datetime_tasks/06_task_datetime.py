# "Вычисление возраста"

# Напишите программу, которая принимает дату рождения пользователя в формате "YYYY-MM-DD" и вычисляет его возраст.

from datetime import date, datetime, timedelta


def get_age(birthday_str: str) -> int:
    start_date = datetime.strptime(birthday_str, "%Y-%m-%d")
    end_date = datetime.now()
    years = end_date.year - start_date.year

    # Проверяем, наступил ли день рождения в текущем году
    # Если конечная дата раньше, чем день рождения в текущем году,
    # то полный год еще не прошел, и нужно вычесть 1.
    if ((end_date.month < start_date.month) or
            (end_date.month == start_date.month and end_date.day < start_date.day)):
        years -= 1

    return years


print(get_age("2000-01-10"))  # 25
print(get_age("2000-05-21"))  # 25
print(get_age("2000-05-20"))  # 25
print(get_age("2000-05-22"))  # 24
