def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_gen()
fib_int = []
count = 0
print_cont = [4, 19, 9999, 99999]
for _ in range(100_000):
    next(fib)
    count += 1
    for i in print_cont:
        if count == i:
            print(next(fib))
