a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
# c = input('Какая операция будет происходить: ')


def dec_calc(func):
    def wrapper(*args):
        first, second = args
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first > second:
            return func(second, first, '-')
        elif second > first:
            return func(first, second, '/')
        elif first == second:
            return func(first, second, '+')
    return wrapper


@dec_calc
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return round(first / second, 2)
    elif operation == '*':
        return first * second


print(calc(a, b))
