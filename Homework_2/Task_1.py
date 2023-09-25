# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

num = int(input("Введите целое число: "))
num_hex = ''

print("Результат встроенной функции: " + hex(num))

while num != 0:
    a = num % 16
    if a < 10:
        num_hex = str(a) + num_hex
    elif a == 10:
        num_hex = 'a' + num_hex
    elif a == 11:
        num_hex = 'b' + num_hex
    elif a == 12:
        num_hex = 'c' + num_hex
    elif a == 13:
        num_hex = 'd' + num_hex
    elif a == 14:
        num_hex = 'e' + num_hex
    else:
        num_hex = 'f' + num_hex
    num = num // 16

print("Результат написанной программы: " + num_hex)
