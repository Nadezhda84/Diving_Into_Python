# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math

fraction_1 = input("Введите строку вида a/b, где a и b - целые числа: ")
fraction_2 = input("Введите строку вида a/b, где a и b - целые числа: ")

str_1 = fraction_1.split("/")
str_2 = fraction_2.split("/")


# Функция сокращения дробей
def reducing_fractions(numerator, denominator):
    num = min(numerator, denominator)
    for i in range(2, num + 1):
        x = math.gcd(numerator, denominator)
        numerator = int(numerator / x)
        denominator = int(denominator / x)
    return numerator, denominator


print()
print("Результат написанной программы: ")

# Сложение дробей
if str_1[1] == str_2[1]:  # Если знаменатели дробей совпадают
    a = int(str_1[0]) + int(str_2[0])
    b = int(str_1[1])
    a, b = reducing_fractions(a, b)
    print(f"{fraction_1} + {fraction_2} = {a}/{b}")
else:  # Если знаменатели дробей не совпадают
    a = int(str_1[0]) * int(str_2[1]) + int(str_2[0]) * int(str_1[1])
    b = int(str_1[1]) * int(str_2[1])
    a, b = reducing_fractions(a, b)
    print(f"{fraction_1} + {fraction_2} = {a}/{b}")

# Произведение дробей
a = int(str_1[0]) * int(str_2[0])
b = int(str_1[1]) * int(str_2[1])
a, b = reducing_fractions(a, b)
if b == 1:
    print(f"{fraction_1} * {fraction_2} = {a}")
else:
    print(f"{fraction_1} * {fraction_2} = {a}/{b}")

print()
print("Результат встроенной функции: ")
print('{} + {} = {}'.format(Fraction(fraction_1), Fraction(fraction_2),
                            Fraction(fraction_1) + Fraction(fraction_2)))
print('{} * {} = {}'.format(Fraction(fraction_1), Fraction(fraction_2),
                            Fraction(fraction_1) * Fraction(fraction_2)))
