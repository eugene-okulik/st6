def repeat_me(func):
    def wrapper(*args, count):
        for _ in range(count):
            func(*args)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
