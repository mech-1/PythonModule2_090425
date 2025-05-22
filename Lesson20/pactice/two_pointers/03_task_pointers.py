# Дана строка.
# Проверить, является ли она палиндромом (читается одинаково в обоих направлениях).
# Важно! Решите задачу, без использования среза

#          l r
string = "swsosw"

left = 0
right = len(string) - 1
is_palindrome = True

while left < right:
    if string[left] != string[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

if is_palindrome:
    print("строка палиндром")
else:
    print("строка не палиндром")