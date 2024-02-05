a = 'результат операции: 42'
b = 'результат операции: 54'
c = 'результат работы программы: 209'
d = 'результат работы программы: 2'


def plus_ten(num):
    num_ind = num.index(':') + 2
    num_plus_ten = int(num[num_ind:]) + 10
    print(num_plus_ten)


plus_ten(a)
plus_ten(b)
plus_ten(c)
plus_ten(d)
