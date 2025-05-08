# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
from fractions import Fraction as F

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# n = '1 5/6 + 4/7'
# n = '1 2/3 - -1 1/2'
# n = '2 5/6 - 4/7'
# n = '-2/3 - -2'
n = '-2/3 + -2'
op = ''

n = input('Введите выражение с дробями : ')

def make_fract(fract):
    if ' ' in fract:
        tmp_fract = fract.split(' ')
        if '-' in fract:
            return F(tmp_fract[0]) - F(tmp_fract[1])
        else:
            return F(tmp_fract[0]) + F(tmp_fract[1])
    return fract


def calculate(fractions, operation):
    negative_sign = ""
    fractions = list(map(make_fract, fractions))
    if operation == '+':
        result = F(fractions[0]) + F(fractions[1])
    else:
        result = F(fractions[0]) - F(fractions[1])
    if result.numerator < 0:
        negative_sign = "-"
    if abs(result.numerator) >= result.denominator:
        result_int = abs(result.numerator) // result.denominator
        result_numerator = abs(result.numerator) % result.denominator
        if result_numerator == 0:
            return f'{negative_sign}{result_int}'
        return f'{negative_sign}{result_int} {result_numerator}/{result.denominator}'
    else:
        return result

if ' + ' in n:
    fractions = n.split(' + ')
    op = '+'
else:
    fractions = n.split(' - ')
    op = '-'

print(f"Результат: {calculate(fractions, op)}")
