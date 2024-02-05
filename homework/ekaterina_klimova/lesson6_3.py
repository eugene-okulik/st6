s1 = 'результат операции: 42'
s2 = 'результат операции: 514'
s3 = 'результат работы программы: 9'


def sum(a):
    b = a.split(':')
    c = int(b[1]) + 10
    return c


print(sum(s1))
print(sum(s2))
print(sum(s3))
