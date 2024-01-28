my_dict = {'tuple': ('Hello', 1000, "I'm from Belarus", 1, 2), 'list': [
    'Hey', 3000, "Like", 15, 20], 'dict': {
    'salary': 2000, 'country': 'Belarus', 'age': 36, 'pets': 'cat', 'address': 'str'}, 'set': {
    1, 5, 'Hello', 10, 15}}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
last_element = my_dict['tuple'][-1]
print(last_element)

# Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент, удалите второй элемент списка
my_dict['list'].append('Element is added')
my_dict['list'].pop(2)
# print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’: добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict['dict']['i am a tuple'] = 10
my_dict['dict'].pop('salary')
# print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество, удалите элемент из множества
my_dict['set'].add('Add')
my_dict['set'].remove('Add')
# print(my_dict['set'])

print(my_dict)
