# Совет: сначала считайте все цены из файла, сохраните в список,
# преобразовав каждую цену к числу(цены в файле хранятся в виде строк)
# А затем, работам с привычным списком, выполните задания
prices = []
path = "data/sold.txt"

with open(path, "r") as file:
    for line in file:
        prices += line.split()

print(prices)
prices = list(map(float, prices))
print("Общая сумма", sum(prices))
print("Цена самого дорого товара", max(prices))
print("Цена самого дешевого товара", min(prices))