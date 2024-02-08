# Ряд Фибаначчи в генераторе
def gen_fiba():
    list_fiba = [0, 1, 1, ]
    for i in range(2, 100001):
        fiba = list_fiba[-1] + list_fiba[-2]
        list_fiba.append(fiba)
    yield list_fiba
    print(list_fiba[5])
    print(list_fiba[200])
    print(list_fiba[1000])
    print(list_fiba[100000])


print(list(gen_fiba()))
