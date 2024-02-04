def process_result(result):
    number = int(result.split(":")[-1].strip())
    return number + 10


results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for result in results:
    print(process_result(result))
