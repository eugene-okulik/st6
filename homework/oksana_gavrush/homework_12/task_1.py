from datetime import datetime

while True:
    date_input = input('Please enter the date in the format (YYYY-MM-DD): ')

    try:
        date = datetime.strptime(date_input, '%Y-%m-%d')
        date_without_time = date.date()
        print('Successfully converted date to Python format:', date_without_time)
        break
    except ValueError:
        print('Incorrect date format. Please enter the date in the format (YYYY-MM-DD)')
