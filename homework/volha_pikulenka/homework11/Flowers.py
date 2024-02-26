class Flowers:
    def __init__(self, name: str, price: int, color: str, avr_lifetime_in_days: int):
        self.name = name
        self.price = price
        self.color = color
        self.avr_lifetime_in_days = avr_lifetime_in_days

    def flower_info(self):
        return (self.name, self.price, self.color, self.avr_lifetime_in_days)

    def flower_desc(self):
        print((f'Name: {self.name.title()}, Price: {self.price}, Color: {self.color}, '
             + f'Lifetime: {self.avr_lifetime_in_days}'))


red_rose = Flowers('rose', 20, 'red', 10)
white_rose = Flowers('rose2', 30, 'white', 11)
daisies = Flowers('daisies', 40, 'white-yellow', 8)
daffodils = Flowers('daffodils', 30, 'bright-yellow', 15)


class Houseplants(Flowers):
    def __init__(self, name: str, price: int, color: str, avr_lifetime_in_days: int,
                 is_houseplant=True):
        super().__init__(name, price, color, avr_lifetime_in_days)
        self.is_houseplant = is_houseplant

    def flower_desc(self):
        print((f'Name: {self.name.title()}, Price: {self.price}, '
             + f'Color: {self.color}, Lifetime: {self.avr_lifetime_in_days}, '
             + f'Hoseplant: {self.is_houseplant}'))


viola = Houseplants('viola', 44, 'violet', 365, True)
petunia = Houseplants('petunia', 33, 'pink', 44, False)

viola.flower_desc()
red_rose.flower_desc()
