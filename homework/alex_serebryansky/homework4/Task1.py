my_dict = {
    'tuple': (1, 'two', 3.0, 'four', True),
    'list': [1, 'two', 3.0, 'four', True],
    'dict': {'value_1': 1, 'value_2': 'two', 'value_3': 3.0, 'value_4': 'four', 'value_5': True},
    'set': {1, 'two', 3.0, 'four', True}
}

print(f"Last element in tuple is - {my_dict['tuple'][-1]}\n")

my_dict['list'].append(False)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = (5, 'six')
my_dict['dict'].pop('value_5')

my_dict['set'].add('some element')
my_dict['set'].remove(True)

for key, value in my_dict.items():
    print(f"{key}: {value}")
