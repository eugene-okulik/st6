res_1 = "результат операции: 42"
res_2 = "результат операции: 514"
res_3 = "результат работы программы: 9"

num1 = int(res_1[res_1.index(':') + 2:]) + 10
num2 = int(res_2[res_2.index(':') + 2:]) + 10
num3 = int(res_3[res_3.index(':') + 2:]) + 10

print(num1)
print(num2)
print(num3)
