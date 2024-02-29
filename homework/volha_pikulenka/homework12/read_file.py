import os


repo_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(repo_path)
path_to_file = os.path.join(repo_path, 'eugene_okulik', 'Lesson_12', 'data.txt')
print(path_to_file)

try:
    with open(path_to_file, 'r', encoding='utf-8') as opened_file:
        data = opened_file.read()
        print(data)
        for word in data:
            if word.istitle():
                print(word[0],)
except (FileNotFoundError) as err:
    print(err)
