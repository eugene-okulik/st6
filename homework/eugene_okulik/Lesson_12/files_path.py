import os
# from utils.home_path import repo_path


repo_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

path_to_file = os.path.join(repo_path, 'homework', 'alex_serebryansky', 'file.txt')
print(path_to_file)

with open(path_to_file, 'r', encoding='utf-8') as open_files:
    data = open_files.read()

print(data)
