text = ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']


def func_number(num):
    for i in text:
        number = int(i.split()[-1]) + num
        print(number)


func_number(10)
