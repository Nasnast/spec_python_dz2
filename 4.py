# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.

import fractions
import math

frac_1 = str(input("Введите первое число вида a/b - ")).split("/")
frac_2 = str(input("Введите второе число вида a/b - ")).split("/")


sum_frac = [
    int(frac_1[0]) * int(frac_2[1]) + int(frac_2[0]) * int(frac_1[1]),
    int(frac_1[1]) * int(frac_2[1]),
]
nod = math.gcd(sum_frac[0], sum_frac[1])
sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]

mult_frac = [int(frac_1[0]) * int(frac_2[0]), int(frac_1[1]) * int(frac_2[1])]
nod = math.gcd(mult_frac[0], mult_frac[1])
mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]

firstfraction = fractions.Fraction(int(frac_1[0]), int(frac_1[1]))
secondfraction = fractions.Fraction(int(frac_2[0]), int(frac_2[1]))
result3 = firstfraction + secondfraction
result4 = firstfraction * secondfraction

print(f"Cумма дробей = {sum_frac[0]}/{sum_frac[1]}")
print(f"ПРОВЕРКА: Cумма дробей = {result3}")
print(f"Произведение дробей = {mult_frac[0]}/{mult_frac[1]}")
print(f"ПРОВЕРКА: Произведение дробей = {result4}")
