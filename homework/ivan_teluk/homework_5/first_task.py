sentences = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' +
             'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

sentences = sentences.split()
new_sentences = []

for sentence in sentences:
    if sentence.endswith(','):
        sentence = sentence.replace(',', 'ing') + ','
    elif sentence.endswith('.'):
        sentence = sentence.replace('.', 'ing') + '.'
    else:
        sentence = sentence + 'íng'
    new_sentences.append(sentence)

new_sentences = ' '.join(new_sentences)
print(new_sentences)
