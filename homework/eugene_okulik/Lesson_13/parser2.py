with open('data.txt', 'r', encoding='utf-8') as data_file:
    data = data_file.read()

features = {}

for section in data.split('\n\n'):
    content = section.strip().splitlines()
    key, *values = content
    features[key] = values


print(features)
