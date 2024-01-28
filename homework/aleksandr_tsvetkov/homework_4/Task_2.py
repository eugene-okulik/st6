text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

# С помощью срезов и метода index получите из каждой строки с результатом число.
# Прибавьте к полученному числу 10, результат сложения распечатайте.

index_result = text1.index(':') + 2     # Индекс числа
number = int(text1[index_result:]) + 10     # Извлечение числа и получение суммы с числом 10
print(number)

index_result2 = text2.index(':') + 2
number2 = int(text2[index_result2:]) + 10
print(number2)

index_result3 = text3.index(':') + 2
number3 = int(text3[index_result3:]) + 10
print(number3)


#



