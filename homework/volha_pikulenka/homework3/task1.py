# Напишите программу, которая спрашивает:

# как вас зовут?
# что вы хотите купить?
# сколько это стоит?
# сколько у вас есть?
# сколько можете отложить в месяц?
# В результате программа должна распечатать, например, такое:

# Привет, Петя. На покупку Ferrari тебе не хватает 1000000

# Возможность совершения покупки: False

# До покупки осталось 200 месяцев

# !! Для выполнения этого задания не нужны условия !!

name = str(input('What is your name?:'))
desired_product = str(input('What would you like to buy?:'))
product_price = float(input(f'How much does {desired_product} cost?:'))
have_money = float(input('How much money do you have?:'))
can_save_money_per_month = float(input('How much money could you save per month?:'))

can_buy = have_money >= product_price
money_to_add = product_price - have_money
months_to_save_money = ((product_price - have_money) / can_save_money_per_month) + 1

print(f'\nHey, {name}! To buy {desired_product} you need to add {money_to_add}.')
print(f'Can buy {desired_product}: {can_buy}.')
print(f'To buy {desired_product} you need {int(months_to_save_money)} more months.')
