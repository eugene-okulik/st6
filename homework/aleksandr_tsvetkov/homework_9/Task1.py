def print_finished(func):
    def wrapper(*args, **kwargs):
        print('*-*-*-*-*')
        func(*args, **kwargs)
        print('*-*-*-*-*')
        print('Finished')
    return wrapper


@print_finished
def func1(*args):
    print(args)


func1('Hello!')
