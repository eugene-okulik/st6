# Задание №1 - "Угадайка"
user_num = input("Угадайте цифру: ")

while user_num != '5':
    print(f'Вы ввели цифру {user_num}')
    user_num = input("Угадайте цифру: ")

print("Вы угадали цифру.")
