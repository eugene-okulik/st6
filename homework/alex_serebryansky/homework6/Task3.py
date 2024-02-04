result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

results = [result_1, result_2, result_3]


def some_function(list_of_results: list, addendum: int):
    for result in list_of_results:
        print(int(result.split()[-1]) + addendum)


some_function(results, addendum=10)
