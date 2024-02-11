my_dict = {
  'tuple': (1, 3, True, None, False, 43, 22),
  'list': [17, 22, False, 33, 'bimbambam', True, 15],
  'dict': {'one': '1', 'two': 2, 'three': 3, 'four': 4.2, 'five': None, 'six': True, 'seven': [1, 4]},
  'set': {3, 5, 15, 25, 32, 66}
}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
my_dict['list'].append('New element')
# удалите второй элемент списка
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict']['i am a tuple'] = (5, 15, 25)
# удалите какой-нибудь элемент
my_dict['dict'].pop('one')
# print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
my_dict['set'].add(99)
# удалите элемент из множества
my_dict['set'].remove(66)
print(my_dict['set'])
