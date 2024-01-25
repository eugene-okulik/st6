name = input(print("как вас зовут?"))

purchase = input(print("что вы хотите купить?"))

cost = float(input(print("сколько это стоит?")))

cash = float(input(print("сколько у вас есть?")))

saving = float(input(print("сколько можете отложить в месяц?")))

print(f'Привет, {name}. На покупку {purchase} тебе не хватает {cash - cost}')
print(f'Возможность совершения покупки: {(cash - cost) >= 0}')
print(f'До покупки осталось {(cost - cash)/saving} месяцев')

