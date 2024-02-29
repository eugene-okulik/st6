import datetime


while True:
    init_date = input('Please enter date in format "dd.mm.yy"\n')
    try:
        py_date = datetime.datetime.strptime(init_date, '%d.%m.%Y')
        print('Thanks, meatbag')
        break
    except (ValueError):
        print('Wrong format, try again.')
