def repeat_me(count):
    def dec(func):

        def inner(*agrs):
            for _ in range(count):
            func(*agrs)
        return inner
    return dec


@repeat_me(count=2)
def example(text):
    print(text)

example('print me')
