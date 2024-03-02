import csv


with open('data.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)


with open('data.csv', newline='') as csv_file:
    file_data2 = csv.DictReader(csv_file)
    for line in file_data2:
        print(line)
