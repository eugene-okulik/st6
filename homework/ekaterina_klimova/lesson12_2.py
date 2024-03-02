import os

repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

path_to_file = os.path.join(repo_path, 'st6', 'homework', 'eugene_okulik', 'hw_12', 'data.txt')
print(path_to_file)

mass = []
with open(path_to_file, 'r', encoding='utf-8') as open_files:
    data = open_files.read()
    for i in data:
        if i.isupper():
            mass.append(i)
print(mass)
