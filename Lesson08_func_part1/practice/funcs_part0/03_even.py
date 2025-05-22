# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False


def is_even(n):
    return n % 2 == 0

n = int(input("n: "))

if is_even(n):
    print("Число четное")
else:
    print("Число не четное")


s = "hello"