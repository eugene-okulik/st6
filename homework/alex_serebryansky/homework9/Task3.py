def calc_me(func):
    def wrapper(*args, **kwargs):
        if '+' in args or '-' in args or '/' in args or '*' in args:
            if args[0] < 0 or args[1] < 0:
                args = tuple(list(args)[:2] + ["*"] + list(args)[3:])
                print('Answer is:', func(*args, **kwargs))
            elif args[0] > args[1]:
                args = tuple(list(args)[:2] + ["-"] + list(args)[3:])
                print('Answer is:', func(*args, **kwargs))
            elif args[0] < args[1]:
                args = tuple(list(args)[:2] + ["/"] + list(args)[3:])
                print('Answer is:', func(*args, **kwargs))
            elif args[0] == args[1]:
                args = tuple(list(args)[:2] + ["+"] + list(args)[3:])
                print('Answer is:', func(*args, **kwargs))
            else:
                print('Answer is:', func(*args, **kwargs))
        else:
            print('Only the following operations are available: +, -, *, /')

    return wrapper


@calc_me
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return 'Only the following operations are available: +, -, *, /'


first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
operation = input('Enter math operation: ')
calc(first_num, second_num, operation)
