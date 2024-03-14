# Чтение файла
import os

my_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

path_to_file = os.path.join(my_path, 'st6', 'homework', 'eugene_okulik', 'hw_12', 'data.txt')
print(path_to_file)

with open(path_to_file, 'r', encoding='utf-8') as open_file:
    my_data = open_file.read()

for i in my_data:
    if i.istitle():
        print(i)


