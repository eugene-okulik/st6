# Задание №1
my_string = \
    ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
     " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
     )

list_from_my_string = my_string.split()
print(list_from_my_string)

for word in list_from_my_string:
    if word.endswith(','):
        word = (word[:-1] + 'ing' + ',')
    elif word.endswith('.'):
        word = (word[:-1] + 'ing' + '.')
    else:
        word = word + 'ing'
    print(word)
