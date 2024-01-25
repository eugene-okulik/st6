# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math

a = float(input())
b = float(input())
c = math.sqrt(a * a + b * b)
S = 0.5 * a * b

print('Гипотенуза:', c)
print('Площадь:', S)
