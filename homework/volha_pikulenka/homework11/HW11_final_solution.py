class Flowers:
    def __init__(self, name: str, price: int, color: str, avr_lifetime_in_days: int):
        self.name = name
        self.price = price
        self.color = color
        self.avr_lifetime_in_days = avr_lifetime_in_days

    def flower_info(self):
        return (self.name, self.price, self.color, self.avr_lifetime_in_days)

    def flower_desc(self):
        print(f'Name: {self.name.title()}, Price: {self.price}, Color: {self.color},'
              f' Lifetime: {self.avr_lifetime_in_days}')

    def __repr__(self):
        return (f'Flower: {self.name}, Price: {self.price}, Color: {self.color}, '
                f'Lifetime: {self.avr_lifetime_in_days} days\n')


red_rose = Flowers('rose', 20, 'red', 10)
white_rose = Flowers('rose2', 30, 'white', 11)
daisies = Flowers('daisies', 40, 'white-yellow', 8)
daffodils = Flowers('daffodils', 30, 'bright-yellow', 15)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, name):
        '''Добавляем по цветку в букет'''
        return self.bouquet.append(name)

    def print_bouquet_flowers(self):
        """Распечатывает названия всех цветов в букете"""
        for name in self.bouquet:
            print(name.name)

    def bouquet_avr_lifetime_in_days(self):
        """Определение средней жизни букета в днях"""
        total_lifetime = 0
        for flower in self.bouquet:
            total_lifetime += flower.avr_lifetime_in_days
        print(f'Average lifetime is {total_lifetime//len(self.bouquet)} days')

    def sort_name(self):
        '''Сортировка по имени'''
        print(f'Sorted by name {sorted(self.bouquet, key=lambda names: names.name)}')

    def sort_color(self):
        '''Сортировка по цвету'''
        print(f'Sorted by color {sorted(self.bouquet, key=lambda color: color.color)}')

    def sort_lifetime(self):
        '''Сортировка по времени жизни'''
        print(f'Sorted by lifetime '
              f'{sorted(self.bouquet, key=lambda lifetime: lifetime.avr_lifetime_in_days)}')

    def search_flowername_based_by_lifetime(self, lifetime):
        for flower in self.bouquet:
            if flower.avr_lifetime_in_days == lifetime:
                return print(f'{flower.name} has lifetime {lifetime} days')
        return print('Nothing was found')


bouq11 = Bouquet()
bouq11.add_flower(daisies)
bouq11.add_flower(daffodils)

# bouq11.print_bouquet_flowers()
# bouq11.bouquet_avr_lifetime_in_days()
# bouq11.sort_name()
# bouq11.sort_color()
# bouq11.sort_color()
# bouq11.sort_lifetime()
# bouq11.search_flowername_based_by_lifetime(15)
