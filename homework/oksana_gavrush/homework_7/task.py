def gen_fibonacci_numbers(n, a=0, b=1):
    for _ in range(n):
        yield a
        a, b = b, a + b


numbers = []
for i in gen_fibonacci_numbers(100_000):
    numbers.append(i)


print(numbers[5-1])
print(numbers[200-1])
print(numbers[1_000-1])
print(numbers[100_000-1])
