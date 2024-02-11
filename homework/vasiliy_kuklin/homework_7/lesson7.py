# Ряд Фибаначчи в генераторе
def gen_fiba(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


print(list(gen_fiba(5))[-1])
print(list(gen_fiba(200))[-1])
print(list(gen_fiba(1000))[-1])
print(list(gen_fiba(100000))[-1])
