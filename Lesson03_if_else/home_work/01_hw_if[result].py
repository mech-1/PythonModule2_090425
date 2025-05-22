n = int(input("размер шоколадки по горизонтали: "))
m = int(input("размер шоколадки по вертикали: "))
k = int(input("количество долек: "))

if (k % n == 0 or k % m == 0) and (n * m > k):
    print("Да")
else:
    print("Нет")
