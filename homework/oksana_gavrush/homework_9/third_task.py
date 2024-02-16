def arithmetic_operation_decorator(func):
    def wrapper(x, y):
        if x < 0 or y < 0:
            return func(x, y, '*')
        elif x == y:
            return func(x, y, '+')
        elif x > y:
            return func(x, y, '-')
        elif x < y:
            return func(x, y, '/')
    return wrapper


@arithmetic_operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


result = calc(int(input()), int(input()))
print(result)
