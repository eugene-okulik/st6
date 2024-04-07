import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="dir name")
parser.add_argument("--text", help="Text find")
parser.add_argument("-date", help="Date %Y-%m-%d %H:%M:%S")
args = parser.parse_args()
log_dir = args.dir
find_text = args.text
find_date = args.date

# Обход файлов в каталоге с помощью iterdir
directori = pathlib.Path(log_dir)

# Команда для терминала:
# запусть из папки с файлом (venv) poweruser@macair-mdev homework_logs_lite %
# cd ~/Documents/test_project/st6/homework/vasiliy_kuklin/homework_logs_lite
# python3 analyzer.py ~/Documents/test_project/st6/homework/eugene_okulik/data/logs/
# --text "spring" -date "2022-02-03 09:07:31"

files = [file.name for file in directori.iterdir() if file.is_file()]
for file in files:
    with open(f'{log_dir}{file}', 'r', encoding='utf-8') as file_open:
        lines = file_open.read()

        if find_text and find_date in lines:
            print(f"лог {find_text} найден в файле {file}")
            index_find_txt = lines.find(find_text)
            print(index_find_txt)
            if index_find_txt >= 100:
                print(lines[index_find_txt - 100:index_find_txt + 100])
            elif index_find_txt <= (len(lines) - 1) - 100:
                print(lines[index_find_txt + 100:])
