# Задание 3

def dekor(func):
    def wrapper(*args):
        first, second = args
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first >= 0 and first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        print(f'operation= {operation}')
        print(func(first=first, second=second, operation=operation))
        func(first=first, second=second, operation=operation)
    return wrapper


@dekor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    elif operation == '**':
        return first ** second


first = int(input('Input first: '))
second = int(input('Input second: '))
print(calc(first, second))
