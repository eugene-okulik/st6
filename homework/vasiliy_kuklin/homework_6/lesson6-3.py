# Задание №3
first = "результат операции: 42"
second = "результат операции: 54"
third = "результат работы программы: 209"
fourth = "результат: 2"

def calc_num_in_strings(texts):
    text = texts.split(': ')
    result = (int(text[1]) + 10)
    print(result)
    return result

calc_num_in_strings(first)
calc_num_in_strings(second)
calc_num_in_strings(third)
calc_num_in_strings(fourth)
