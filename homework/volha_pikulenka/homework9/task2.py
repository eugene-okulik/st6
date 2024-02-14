def repeat_me(count):
    def true_decorator(func):
        def wrapper(*args, **kwargs):
            iter = 0
            while iter!=count:
                func(*args, **kwargs)
                iter += 1
        return wrapper
    return true_decorator


@repeat_me(3)
def example(text):
    print(text)

example('print me')
