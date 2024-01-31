text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

text_list = text.split()
new_text_list = []
for word in text_list:
    if word.endswith(',') or word.endswith('.'):
        word = word[:(len(word)-1)] + 'ing' + word[(len(word)-1):]
    else:
        word = word + 'ing'

    new_text_list.append(word)

result = ' '.join(new_text_list)
print(result)
