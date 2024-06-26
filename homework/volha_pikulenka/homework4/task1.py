# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами:
# ‘tuple’, ‘list’, ‘dict’, ‘set’.
# Для каждого элемента задайте значение соответствующее названию ключа.
# Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения.
# Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию,
# но количество элементов в каждом таком значении должно быть не меньше пяти.
# Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5),
# если список, то не меньше пяти элементов, если словарь,
# то не меньше пяти пар ключ-значение, итд.
my_dict = {}
my_dict['tuple'] = (88, 42, 33, 22, 11)
my_dict['list'] = [1, 5, 11, 'gogo', 3.14]
my_dict['dict'] = {'1': 1, '2': 2, 3: 3, 'foo': 'var', 666: '666'}
my_dict['set'] = {1, 11, 111, 1111, 11111}
# Действия с элементами словаря my_dict:
# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент
tuple_list = my_dict.get('tuple')
print(f'Last item in tuple is: {tuple_list[-1]}')
# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_dict['list'].append('addedElement')
my_dict['list'].pop(1)
# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict'].update({('I am a tuple',): ('tuple', 'here')})
del my_dict['dict'][3]
# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_dict['set'].add(222)
my_dict['set'].discard(11)
# В конце выведите на экран весь словарь
print(f'\nMy dictionary is \n{my_dict}')
