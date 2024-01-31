text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.\n'
'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()
new_words = []

for word in words:
    if word[-1] in [",", "."]:
        punctuation = word[-1]
        word = word[:-1]
    else:
        punctuation = ""

    new_word = word + "ing" + punctuation
    new_words.append(new_word)

new_text = " ".join(new_words)

print(new_text)




