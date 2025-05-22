# "Работа со списком товаров"
#
# Создайте список словарей, представляющих несколько товаров (минимум 4 товара).
# Выведите на экран нумерованный список всех названий товаров

items = [
    {"name": "Брюки", "cost": 35, "quantity": 10},
    {"name": "Кепка", "cost": 5, "quantity": 8},
    {"name": "кеды", "cost": 8, "quantity": 100},
    {"name": "Рубашка", "cost": 12, "quantity": 16},
]

# i = 1
for i, item in enumerate(items, 1):
    print(f"{i} {item["name"]}")


# count = 1
# for product in products:
#     print(str(count) + ". " + product["name"])
#     count += 1