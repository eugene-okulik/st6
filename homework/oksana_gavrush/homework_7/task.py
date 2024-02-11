def get_fibonacci():
    a, b = 0, 1
    while True:
        yield b
        b = a + b
        a = b - a


position_num = {
    5: "Пятое число Фибоначчи",
    200: "Двухсотое число Фибоначчи",
    1_000: "Тысячное число Фибоначчи",
    100_000: "Стотысячное число Фибоначчи"
}

for counter, find_value in enumerate(get_fibonacci(), start=2):
    if counter in position_num:
        print(f'{position_num[counter]}: {find_value}')
    if counter == 100000:
        break
