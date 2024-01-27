my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'set': {11, 12, 13, 14, 15},
    'dict' : {'one': '1', 'two': '2', 'three' : '3', 'four': '4', 'five' : '5'}
    }

# Для того, что хранится под ключом ‘tuple’:выведите на экран последний элеме
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
my_dict['list'].append(11)
print(my_dict['list'])

# удалите второй элемент списка
my_dict['list'].remove(7)
print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'].update({'i am a tuple': 1})
print(my_dict['dict'])
# удалите какой-нибудь элемент
my_dict['dict'].pop('one')
print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
my_dict['set'].add(0)
print(my_dict['set'])
# удалите элемент из множества
my_dict['set'].remove(15)
print(my_dict['set'])