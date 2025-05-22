a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

perimeter = a + b + c
p = (a + b + c) / 2
square = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"P = {perimeter}")
print(f"S = {square}")

# Ctrl + Alt + L - автоформат по PEP-8
