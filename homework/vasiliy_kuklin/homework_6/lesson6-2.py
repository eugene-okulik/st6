# Задание №2
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for k,v in words.items():
    for i in range(v):
        print(k, end='')
    print('')
