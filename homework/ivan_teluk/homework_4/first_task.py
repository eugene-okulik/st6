my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['first', 'second', 'third', 'fourth', 'fifth'],
    'dict': {'dict1': 'value1', 2: 'value2', 3: 'value3', 4: 'value4', 5: 'value5'},
    'set': {'set1', 'set2', 'set3', 'set4', 'set5'}
    }
print(my_dict['tuple'][-1])     # Выводим на экран последний элемент из значения ключа tuple
my_dict['list'].append('sixth')     # Добавляем элемент в конец списка значения ключа list
my_dict['list'].pop(1)      # Удаляем второй элемент из значения ключа list
my_dict['dict'].update({('i am a tuple',): 1})      # Добавляем кортеж в качестве ключа в значение ключа dict
my_dict['dict'].pop('dict1')        # Удаление значение для ключа dict1
my_dict['set'].add('set6')      # Добавление элемента в множество ключа set
my_dict['set'].discard('set1')      # Удаление элемента из множества ключа set
print(my_dict)
