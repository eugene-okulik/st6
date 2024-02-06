import random

secret_number = random.randint(1, 10)

print("Давайте сыграем в угадайку! Я загадал число от 1 до 10.")

while (guess := int(input("Попробуйте угадать число: "))) != secret_number:
    print("Попробуйте снова.")

print("Поздравляю! Вы угадали!")
