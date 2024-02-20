# Задание №1
def finish_me(func):
    def wrapper(args):
        func(args)
        print('finished')
    return wrapper


@finish_me
def pechatnik(text):
    print(text)


print(pechatnik('Hello!'))
