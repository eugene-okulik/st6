my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'set': {11, 12, 13, 14, 15},
    'dict' : {'one': '1', 'two': '2', 'three' : '3', 'four': '4', 'five' : '5'}
    }

print(my_dict['tuple'][-1])
my_dict['list'].append(11)
print(my_dict['list'])
my_dict['list'].remove(7)
print(my_dict['list'])
my_dict['dict'].update({'i am a tuple': 1})
print(my_dict['dict'])
my_dict['dict'].pop('one')
print(my_dict['dict'])
my_dict['set'].add(0)
print(my_dict['set'])
my_dict['set'].remove(15)
print(my_dict['set'])
print(my_dict)
