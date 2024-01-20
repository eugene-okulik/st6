a = int(input('Insert the length of the first leg: '))
b = int(input('Insert the length of the second leg: '))

hypotenuse_length = (a ** 2 + b ** 2) ** (1 / 2)
square = a * b * 1 / 2
print(f'The length of hypotenuse is {hypotenuse_length}\n'
      f'The square of triangle is {square}')
