result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

print(int(result_1[(result_1.index(':') + 2):]) + 10)
print(int(result_2[slice((result_2.index(':') + 2), None)]) + 10)
print(int(result_3[(result_3.index(':') + 2):]) + 10)
