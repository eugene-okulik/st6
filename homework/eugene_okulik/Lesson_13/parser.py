with open('data.txt', 'r', encoding='utf-8') as data_file:
    data = data_file.read()


print(data)

features = {}

lines = data.splitlines()
print(lines)

new_categ = True
current_categ = None
for line in lines:
    if new_categ is True:
        features[line] = []
        current_categ = line
        new_categ = False
    elif line == '':
        new_categ = True
    else:
        features[current_categ].append(line)


print(features)
