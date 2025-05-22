# "Название сегодняшнего дня недели"

# Напишите функцию, которая возвращает название сегодняшнего дня недели на русском языке
# (например, "понедельник", "вторник" и т.д.) с учетом текущей даты.

import locale
from datetime import date


def get_today_day_name(today: date) -> str:
    """Возвращает название сегодняшнего дня недели на русском языке."""
    day_names = {1: 'понедельник', 2: 'вторник', 3:'среда'}
    return day_names[today.isoweekday()]


def get_today_day_name_v2(today: date) -> str:
    # Установим локаль на русский для получения названий на русском языке
    # Это может зависеть от вашей операционной системы и ее настроек локалей.
    # На Windows это может быть 'ru_RU' или 'Russian_Russia.1251'
    # На Linux/macOS это чаще 'ru_RU.UTF-8' или 'ru_RU'
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    return today.strftime("%A")



today = date.today()
day_name = get_today_day_name_v2(today)
print(day_name)