# Даны числа x и y. Получить x − y / 1 + xy и вывести на экран


x = int(input('Ввести первое число: '))
y = int(input('Ввести второе число: '))
z = x - y / 1 + x * y
print(f'Результат: {z}')