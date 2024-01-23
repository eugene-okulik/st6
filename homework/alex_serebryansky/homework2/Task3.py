a = int(input('Insert first number: '))
b = int(input('Insert second number: '))

average = (a + b) / 2
geo_average = (a * b) ** 0.5

print(f'The average of {a} and {b} is {average}\n'
      f'The geometric average of {a} and {b} is {geo_average}')
