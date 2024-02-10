import sys

sys.set_int_max_str_digits(0)


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for x in fibonacci():
    if count == 5 or count == 200 or count == 1000 or count == 100000:
        print(x)
    elif count > 100000:
        break
    count += 1
