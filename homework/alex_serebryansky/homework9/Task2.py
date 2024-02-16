def repeat_me(func):
    def wrapper(*args, count: int, **kwargs):
        if count <= 0:
            print('The count can not be less than zero or equal to zero')
        elif count == 1:
            func(*args, **kwargs)
        else:
            [func(*args, **kwargs) for _ in range(count)]
        print('finished')

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=10)
