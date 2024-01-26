name = input('Как вас зовут? ')
sale = input('Что вы хотите купить? ')
how_match = int(input('Сколько это стоит? '))
how_money = int(input('Сколько у вас есть? '))
how_money_month = int(input('Сколько можете отложить в месяц? '))
itog = how_match - how_money
month = (how_match - how_money) // how_money_month

print(f'Привет, {name}. На покупку {sale} тебе не хватает {itog}')
print(f'Возможность совершения покупки: {how_money >= how_match}')
print(f'До покупки осталось {month} месяцев')
