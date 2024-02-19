def print_hello_after(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('finished')
    return wrapper


@print_hello_after
def example(text):
    print(text)


example(input())
