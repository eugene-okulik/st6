def repeat_me(func):
    def wrapper(*args, **kwargs):
        run_count = kwargs.pop("run_count")
        for i in range(run_count):
            func(*args, **kwargs)
    return wrapper


@repeat_me
def example(text):
    print(text)


example(input(), run_count=5)
