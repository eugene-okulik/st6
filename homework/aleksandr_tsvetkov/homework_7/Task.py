# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

def fibonacci():
    prev_num = 0
    next_num = 1
    while True:
        yield prev_num
        old_prev_num = prev_num
        prev_num = next_num
        next_num = old_prev_num + next_num


counter = 0
for i in fibonacci():
    # print(i)
    counter += 1
    if counter == 5:
        print(f'Пятое число Фибоначчи: {i}')
    elif counter == 200:
        print(f'Двухсотое число Фибоначчи: {i}')
    elif counter == 1000:
        print(f'Тысячное число Фибоначчи: {i}')
    elif counter == 100000:
        print(f'Стотысячное число Фибоначчи: {i}')
        break
