import os

repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(repo_path)

path_to_file = os.path.join(repo_path, 'homework', 'eugene_okulik', 'hw_12', 'data.txt')
print(path_to_file)


def open_and_read_file(path_to_files):
    with open(path_to_files, 'r', encoding='utf-8') as open_file:
        data = open_file.read()
        for i in data:  # Распечатываем только больщие буквы из файла
            if i.isupper():
                print(i, end='')
    print(f'\n{data}')


open_and_read_file(path_to_file)
