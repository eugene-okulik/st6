def calc(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError) as err:
        print(x, y)
        print(err)
        return 'Some error has happened'
    # except ZeroDivisionError:
    #     return 'Нельзя делить на ноль'
    # except TypeError:
    #     return 'Нужны инты'
    # else:
    #     print('calc successful')


# print(calc(int(input('first')), int(input('second'))))

print(calc(1, 0))
# print(calc('1', '3'))


def calc2(x, y):
    try:
        print(x / y)
    except (ZeroDivisionError, TypeError):
        print(x, y)
        print('Some error has happened')
    else:
        print('calc successful')
    finally:
        print('Calc end')


# print(calc(int(input('first')), int(input('second'))))

calc2(1, 0)
# calc2('1', '3')
calc2(4, 8)


open_file = open('data.txt', 'r', encoding='utf-8')
try:
    data = open_file.read()
    # print(data['sldkjf'])
except ValueError:
    print('sdkjfhskdjfh')
else:
    print(data)
finally:
    open_file.close()
