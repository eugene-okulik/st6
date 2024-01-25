print("как вас зовут?")
name = input()

print("что вы хотите купить?")
purchase = input()

print("сколько это стоит?")
cost = float(input())

print("сколько у вас есть?")
cash = float(input())

print("сколько можете отложить в месяц?")
saving = float(input())

print(f'Привет, {name}. На покупку {purchase} тебе не хватает {cash - cost}')
print(f'Возможность совершения покупки: {(cash - cost) >= 0}')
print(f'До покупки осталось {(cost - cash)/saving} месяцев')

