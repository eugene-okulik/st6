# Задание №2
def repeater(func):
    def wrapper(*args, **kwargs):
        for key, value in kwargs.items():
            if value in kwargs.values():
                for i in range(value):
                    func(*args)

    return wrapper


@repeater
def example(text):
    print(text)


example('print_me', count=3)
