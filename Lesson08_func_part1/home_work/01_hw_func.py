# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if len(ticket_number_str) != 6:
        return False
    part1 = ticket_number_str[:3]
    part2 = ticket_number_str[3:]
    sum_part1 = 0
    sum_part2 = 0
    for el in part1:
        sum_part1 += int(el)
    for el in part2:
        sum_part2 += int(el)

    return sum_part1 == sum_part2

def lucky_ticket_v2(ticket_number):
    # ticket_number = 123456
    # ticket_number % 10 -> 6
    # ticket_number // 10 -> 12345
    sum_part1 = 0
    sum_part2 = 0
    num_digit = 6
    while ticket_number != 0:
        digit = ticket_number % 10
        ticket_number = ticket_number // 10
        if num_digit > 3:
            sum_part2 += digit
        else:
            sum_part1 += digit
        num_digit -= 1

    return sum_part1 == sum_part2



# Тестируем функцию
print(lucky_ticket_v2(123006)) # True
print(lucky_ticket_v2(123206)) # False

print(lucky_ticket_v2(436751)) # True
# print(lucky_ticket(12321))
# print(lucky_ticket(1232123))