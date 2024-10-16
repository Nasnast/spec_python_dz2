# Задание 2. Преобразование числа в шестнадцатеричное представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.

a = int(input("введите число: "))

hex_string_1 = hex(a)  # проверка
print(hex_string_1)

hex_symbols = "0123456789ABCDEF"

if a == 0:
    hex_string = "0"
else:
    minus_a = a < 0
    if minus_a:
        a = -1 * a

hex_string = ""
while a > 0:
    i = a % 16
    hex_string = hex_symbols[i] + hex_string
    a = a // 16

if minus_a:
    hex_string = "-" + "0x" + hex_string

print("0x" + hex_string)
