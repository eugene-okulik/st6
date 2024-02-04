my_dict = \
    {'tuple': (1, 2, 3, 4, 5),
     'list': [1, "paris", None, 2.5, 777],
     'dict': {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5},
     'set': {1, "sport", "solo", False, 5}
     }

# Задание 1
print(my_dict['tuple'][-1])
my_dict['list'].append(888)
my_dict['list'].pop(1)
my_dict['dict'].update({'i am a tuple': 900})
my_dict['dict'].pop('two')
my_dict['set'].add(9)
my_dict['set'].pop()
print(my_dict)

# Задание 2
first = "результат операции: 42"
second = "результат операции: 514"
third = "результат работы программы: 9"

print(int(first[-2:]) + 10)
last_num_second = ((second.index(': ')) + 2)
print(int(second[last_num_second:]) + 10)
last_num_third = ((third.index(': ')) + 2)
print(int(third[last_num_third]) + 10)
