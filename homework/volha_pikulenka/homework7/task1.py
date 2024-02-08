def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_gen()
fib_int = []
for _ in range(100_000):
    fib_int.append(next(fib))

print(fib_int[4])
print(fib_int[199])
print(fib_int[9999])
print(fib_int[99999])
