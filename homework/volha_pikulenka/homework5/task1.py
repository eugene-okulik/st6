init_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
             'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
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
