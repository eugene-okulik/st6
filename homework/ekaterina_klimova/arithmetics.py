from math import sqrt

x, y = int(input()), int(input())
arith = (x + y) / 2
geom = sqrt(x * y)

print(f'average = {arith}, geometric mean = {geom}')
