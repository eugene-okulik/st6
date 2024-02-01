# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте 
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, 
# facilisis vitae semper at, dignissim vitae libero” 
# и после этого выводит получившийся 
# текст на экран. Знаки препинания не должны оказаться внутри слова. 
# Если после слова идет запятая или точка, этот знак препинания должен
# идти после того же слова, но уже преобразованного.

init_text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

split_text = init_text.split()

for word in split_text:
    if word.endswith(','):
        word = word.strip(',') + 'ing,'
    elif word.endswith('.'):
        word = word.strip('.') + 'ing.'
    else:
        word = word + 'ing'
    ing_plus_text = word
    print(ing_plus_text, end=' ')
    