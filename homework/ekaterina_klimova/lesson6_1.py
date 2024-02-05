import random

random_number = random.randint(1, 101)

print('Давай поиграем в угадайку. Мы загадали число от 1 до 100. Попробуй угадай')
while random_number != (n := int(input("Введи число от 1 до 100:"))):
    print('попробуйте снова')
print('Поздравляю! Вы угадали!')
