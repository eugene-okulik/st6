# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
#                 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28. Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
# print(list(hot_days))
new_hot_days = list(hot_days)
print(f'Max temperature: {max(new_hot_days)}')
print(f'Min temperature: {min(new_hot_days)}')
print(f'Average temperature: {round(sum(new_hot_days) / len(new_hot_days))}')
