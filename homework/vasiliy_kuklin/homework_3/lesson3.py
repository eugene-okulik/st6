name = input("Как вас зовут? ")
product = input("Что вы хотите курпить? ")
price = input("Сколько это стоит? ")
money = input("Сколько у вас есть денег? ")
save_money = input("Сколько можете отложить в месяц? ")

sum_price = int(price) - int(money)
mounths = sum_price / int(save_money)
text = 'Привет ' + name.title() + '!' + 'На покупку ' + product.title() + ' тебе не хватает ' + str(sum_price)
print(text)
print(f"Возможность совершения покупки: ")
print(f'{int(sum_price)}' in price)
print(f"До покупки осталось {mounths} месяцев")

