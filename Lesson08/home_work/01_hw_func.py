# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum1 = sum2 = 0
    ticket_number_str = str(ticket_number)
    for i, num in enumerate(ticket_number_str):
        if len(ticket_number_str) / 2 < i:
            sum1 += int(num)
        else:
            sum2 += int(num)
    return sum1 == sum2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
