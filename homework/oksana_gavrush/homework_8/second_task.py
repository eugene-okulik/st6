temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30,
                32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
result = list(filter(lambda x: x if x > 28 else False, temperatures))
print(f'Самая высокая температура {max(result)}')
print(f'Самая низкая температура {min(result)}')
average = sum(result) / len(result)
print(f'Средняя температура {round(average)}')
