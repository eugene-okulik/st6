import os
repo_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
patch_fail = os.path.join(repo_path, 'eugene_okulik', 'hw_12', 'data.txt')
with open(patch_fail, 'r', encoding='utf-8') as file:
    content = list(file.read())
    for letter in content:
        if letter.isupper():
            print(letter, end='')
