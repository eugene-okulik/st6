name = str(input('Как тебя зовут?\n'))
desired_product = str(input('Что ты хочешь купить?\n'))
cost_of_product = float(input(f'Сколько {desired_product} стоит?\n'))
capital = float(input('Какая сумма у тебя уже есть?\n'))
monthly_savings = float(input('Какую сумму можешь откладывать в месяц?\n'))
print(f'Привет {name}! На покупку {desired_product} тебе не хватает', cost_of_product - capital,
      '\nВозможность совершения покупки:', capital >= cost_of_product,
      '\nДо покупки осталось:', (cost_of_product - capital) / monthly_savings, 'мес.')
