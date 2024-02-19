import functools


def repeat_me(func):
    def wrapper(*args, count: int, **kwargs):
        if count <= 0:
            print('The count can not be less than zero or equal to zero')
        elif count == 1:
            func(*args, **kwargs)
        else:
            [func(*args, **kwargs) for _ in range(count)]

    return wrapper


def repeat(count=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            [func(*args, **kwargs) for _ in range(count)]

        return wrapper

    return decorator


# @repeat_me
@repeat(count=5)
def example(text):
    print(text)


# example('print me', count=2)
example('print me')
