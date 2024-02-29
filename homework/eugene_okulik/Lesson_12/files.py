import useful

# open_files = open('data.txt', 'r', encoding='utf-8')
# data = int(open_files.read())
# open_files.close()


with open('data.txt', 'r', encoding='utf-8') as open_files:
    data = open_files.readlines()


for line in data:
    print(line)


with open('data2.txt', 'w', encoding='utf-8') as data2_file:
    data2_file.write('!!!!my text!!!!!')


with open('data3.txt', 'a', encoding='utf-8') as data3_file:
    data3_file.write(f"XXX{useful.random_weather('New York')}\n")
