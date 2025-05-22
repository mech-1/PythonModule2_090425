n = int(input("n: "))

divider = 2
is_prime = True
while divider < n:
    if n % divider == 0:
        is_prime = False
        print(divider)
    divider += 1

if is_prime:
    print("Число простое")