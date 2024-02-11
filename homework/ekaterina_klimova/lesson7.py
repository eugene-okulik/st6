#Напишите функцию-генератор, которая генерирует список чисел фибоначчи
#Распечатайте из этого списка пятое число, двухсотое число, тысячное число, 
#стотысячное число
def gen_fibonacci_numbers(n):
    a, b = 1, 1
    i = 1
    while i <= n:
        yield a
        a, b = b, a + b
        i += 1

count = 0
for i in gen_fibonacci_numbers(100000):
    count += 1
    if count == 5:
        print(i)
    elif count == 200:
        print(i)
    elif count == 1000:
        print(i)
    elif count == 100000:
        print(i)
    