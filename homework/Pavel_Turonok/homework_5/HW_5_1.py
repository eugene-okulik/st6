text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

split_text = text.split()
new_text = []

for i in split_text:
    if i[-1] == '.' or i[-1] == ',':
        new_text.append(i[:-1] + 'ing' + i[-1])
    else:
        new_text.append(i + 'ing')
print(' '.join(new_text))
