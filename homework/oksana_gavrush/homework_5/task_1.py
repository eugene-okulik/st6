text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        + 'facilisis vitae semper at, dignissim vitae libero')
punctuation = ',.'
new_text = []
for word in text.split():
    if word[-1] in punctuation:
        new_text.append(f'{word[:-1]}ing{word[-1]}')
    else:
        new_text.append(f'{word}ing')
print(' '.join(new_text))
