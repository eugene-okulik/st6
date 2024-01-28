my_dict = {'tuple': ("Pinocchio", "malvina", "artemon", "Karabas", "tortilla"),
           'list': ['leech', 'worm', 'caterpillar', 'slug', 'scolopendra'],
           'dict': {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 'set': {1, 2, 3, 4, 5}}

print("tuple: выведите на экран последний элемент")
print(my_dict['tuple'][-1])
print()

print("list: добавьте в конец списка еще один элемент")
r = my_dict['list']
r.append("bug")
print(my_dict['list'])
print()

print("list: удалите второй элемент списка")
del my_dict['list'][1]
print(my_dict['list'])
print()

print("dict: добавьте элемент с ключом ('i am a tuple',) и любым значением")
d = my_dict['dict']
d.update({'i am a tuple': 1})
print(my_dict['dict'])
print()

print("dict: удалите какой-нибудь элемент")
del my_dict['dict'][1]
print(my_dict['dict'])
print()

print("set: добавьте новый элемент в множество")
s = my_dict['set']
s.add("new")
print(my_dict['set'])
print()

print("set: удалите элемент из множества")
my_dict['set'].remove(4)
print(my_dict['set'])

print()
print("Весь словарь")
print(my_dict)
