from datetime import datetime

while True:
    date_t = input("Введите дату в формате (ГГГГ-ММ-ДД):")


    try:
        date_obj = datetime.strptime(date_t, '%Y-%m-%d')
        print("Спасибо! Дата введена корректно: ", date_obj)
        break
    except:
        print("Введите, пожалуйста, дату в формате (ГГГГ-ММ-ДД)")
