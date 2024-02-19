def finish_me(func):

    def inner(*args):
        func(*args)
        print("finished")
    return inner


@finish_me
def example(text):
    print(text)


example('print me')
