result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

result_1_find_num = result_1.find(':') + 2
plus_num_1 = int(result_1[result_1_find_num:]) + 10
print(plus_num_1)

result_2_find_num = result_2.find(':') + 2
plus_num_2 = int(result_2[result_2_find_num:]) + 10
print(plus_num_2)

result_3_find_num = result_3.find(':') + 2
plus_num_3 = int(result_3[result_3_find_num:]) + 10
print(plus_num_3)
