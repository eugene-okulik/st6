def calc_decorator(func):
    def wrapper(*args, **kwargs):

        if args[0] < 0 or args[1] < 0:
            return print(args[0] * args[1])
        # это условие должно быть входом, иначе оно всегда игнорируется

        elif args[0] == args[1]:
            return print(args[0] + args[1])

        elif args[0] > args[1]:
            return print(args[0] - args[1])

        elif args[0] < args[1]:
            return print(args[0] / args[1])

        print(func(*args, **kwargs))

    return wrapper


num1 = int(input('\nEnter the first number: '))
num2 = int(input('\nEnter the second number: '))
oper = input('\nEnter operation type: ')


@calc_decorator
def calc(number1, number2, operation):
    if operation == '+':
        sum = number1 + number2
        return sum
    elif operation == '-':
        substr = number1 - number2
        return substr
    elif operation == '/':
        division = number1 / number2
        return division
    elif operation == '*':
        mult = number1 * number2
        return mult


calc(num1, num2, oper)
