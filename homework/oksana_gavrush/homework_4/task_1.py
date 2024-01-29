type_difference = {'tuple': ('strawberry', 'cherry', 'pear', 'apple', 'grape'),
                   'list': [22, 33, 44, 55, 66],
                   'dict': {'name': 'Jon',
                            'age': 28,
                            'hobbies': 'hockey',
                            'profession': 'engineer',
                            'email': 'super@gmail.com'},
                   'set': {1, 22, 33, 44, 99}}

print(type_difference['tuple'][-1])

type_difference['list'].append(77)
print(type_difference['list'])
type_difference['list'].pop(1)
print(type_difference['list'])

type_difference['dict'][('i am a tuple',)] = ('27.01.2024',)
print(type_difference['dict'])
type_difference['dict'].pop('profession')
print(type_difference['dict'])

type_difference['set'].add(101)
print(type_difference['set'])
type_difference['set'].remove(101)
print(type_difference['set'])
