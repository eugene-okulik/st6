# Ряд Фибаначчи в генераторе
def gen_fiba():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


i = 1
for n in gen_fiba():
    if i == 5 or i == 200 or i == 1000 or i == 100000:
        print(n)
    elif i > 100000:
        break
    i += 1
