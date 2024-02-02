# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero”
# и после этого выводит получившийся текст на экран. Знаки препинания не должны оказаться внутри слова.Если после
# слова идет запятая или точка, этот знак препинания должен идти после того же слова, но уже преобразованного


text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        'facilisis vitae semper at, dignissim vitae libero')
split_from_text = text.split()
new_text = []

for i in split_from_text:
    if i[-1] == '.' or i[-1] == ',':
        new_text.append(i[:-1] + 'ing' + i[-1])
    else:
        new_text.append(i + 'ing')
print(' '.join(new_text))
