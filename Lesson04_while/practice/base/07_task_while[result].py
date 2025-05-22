n = int(input("n: "))

# "1" + "2" -> "12" + "3" -> "123"
line = "1"
i = 1
while i <= n:
    print(line)
    i += 1
    line += str(i)

# n = 4
# 1
# 12
# 123
# 1234