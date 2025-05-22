# "Поиск товара в списке словарей"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Напишите функцию, которая принимает название товара и список словарей в качестве аргументов.
# Функция должна возвращать словарь товара с указанным названием или None, если товар не найден.
# Вызовите функцию для поиска товара и выведите результат.

def find_item_by_name(items: list[dict], name: str) -> dict | None:
    for item in items:
        if item["name"].lower() == name.lower():
            return item

    return None

items = [
    {"name": "Брюки", "cost": 35, "quantity": 10},
    {"name": "Кепка", "cost": 5, "quantity": 8},
    {"name": "кеды", "cost": 8, "quantity": 100},
    {"name": "Рубашка", "cost": 12, "quantity": 16},
]

print(find_item_by_name(items, "Брюки"))
print(find_item_by_name(items, "Носки"))
print(find_item_by_name(items, "кепка"))