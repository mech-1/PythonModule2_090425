n = int(input("n: "))
i = 0
total = 0
while i < n:
    i += 1
    total += i ** 2
# 1 + 4 + 9 + 16
print(f"Сумма цифр на всех этажах = {total}")
