x = float(input('Insert number of X: '))
y = float(input('Insert number of Y: '))
if x * y == -1:
    print('The equation has no solution')
else:
    z = (x - y) / (1 + x * y)
    print(f'The solution is: {z}')
