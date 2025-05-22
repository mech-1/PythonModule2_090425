a = 0
n = int(input("n: "))
summa = 0
while a <= n:
    if a % 2 == 0:
        summa += a
    a += 1

print(summa)