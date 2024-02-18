def choose_me(func):

    def operation(*args):
        a, b, op = args
        if a == b and a > 0 and b > 0:
            op = '+'
        elif a > b > 0:
            op = '-'
        elif 0 < a < b:
            op = '/'
        elif a < 0 or b < 0:
            op = '*'
        return func(a, b, op)
    return operation


@choose_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first, second = int(input()), int(input())
result = calc(first, second, None)
print(result)
