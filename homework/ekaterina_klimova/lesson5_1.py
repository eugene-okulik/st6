s = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
s1 = s.split()
print(s1)
s2 = []
for i in s1:
    if ',' in i:
        a = i.replace(',', 'ing,')
    elif '.' in i:
        a = i.replace('.', 'ing.')
    else:
        a = i + 'ing'
    s2.append(a)
s3 = ' '.join(s2)
print(s3)
