text_1 = 'результат операции: 42'
text_2 = 'результат операции: 514'
text_3 = 'результат работы программы: 9'

print(int(text_1[text_1.index(': ') + 2:]) + 10)
print(int(text_2[text_2.index(': ') + 2:]) + 10)
print(int(text_3[text_3.index(': ') + 2:]) + 10)
