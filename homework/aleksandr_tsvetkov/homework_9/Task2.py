def repeat(func):
    def wrapper(*args, count=1):
        for i in range(count):
            print(func(*args))
    return wrapper


@repeat
def func1(text):
    return text


func1('Finished', count=10)
