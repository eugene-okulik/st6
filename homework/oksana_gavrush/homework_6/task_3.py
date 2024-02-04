def function1(text, num):
    return int(text[text.find(':') + 2:]) + num


for _ in range(4):
    print(function1(input(), 10))
