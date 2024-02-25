def decorator(func):
    def wrapper(*args, **kwargs):
        print('*' * 30)
        return func(*args, **kwargs)
    return wrapper


# Общий класс для цветов
class Flowers:

    def __init__(self, name, color, price, freshness, stem_length):
        self.stem_length = stem_length
        self.freshness = freshness
        self.price = price
        self.name = name
        self.color = color

    def __str__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm')

    def __repr__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm')


# Дочерний класс для Роз
class Rose(Flowers):
    def __init__(self, name, color, price, freshness, stem_length, strips=True):
        super().__init__(name, color, price, freshness, stem_length)
        self.strips = strips

    def __str__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Strips: {self.strips}')

    def __repr__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Strips: {self.strips}')


# Дочерний класс для Тюльпанов
class Tulip(Flowers):
    def __init__(self, name, color, price, freshness, stem_length, variety):
        super().__init__(name, color, price, freshness, stem_length)
        self.variety = variety

    def __str__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Variety: {self.variety}')

    def __repr__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Variety: {self.variety}')


# Дочерний класс для Лилий
class Lily(Flowers):
    def __init__(self, name, color, price, freshness, stem_length, variety):
        super().__init__(name, color, price, freshness, stem_length)
        self.variety = variety

    def __str__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Variety: {self.variety}')

    def __repr__(self):
        return (f'Flower: {self.name}, Color: {self.color}, Price: {self.price}$, Freshness: {self.freshness} days, '
                f'Stem length: {self.stem_length} cm, Variety: {self.variety}')


# Класс для букета
class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

# Метод для определения цены букета
    @decorator
    def bouquet_price(self):
        price = 0
        for flower in self.flowers:
            price += flower.price
        return f'Bouquet price: {price}'

# Метод чтобы распечатать имена цветов в букете
    @decorator
    def print_flower_names_in_bouquet(self):
        for flower in self.flowers:
            print(f'Bouquet: Flowers: {flower.name}, Color: {flower.color}')

# Метод, определяеющий время увядания по среднему времени жизни всех цветов в букете
    @decorator
    def fading_time(self):
        fading = 0
        for flower in self.flowers:
            fading += flower.freshness
        return f'Fading time: {fading // len(self.flowers)} days'

# Метод, сортирующий цветы в букете по свежести, цене, длине стебля, цвету
    def sort_flowers(self, parameter):
        if parameter == 'freshness':
            self.flowers.sort(key=lambda x: x.freshness)
        elif parameter == 'price':
            self.flowers.sort(key=lambda x: x.price)
        elif parameter == 'stem_length':
            self.flowers.sort(key=lambda x: x.stem_length)
        elif parameter == 'color':
            self.flowers.sort(key=lambda x: x.color)
        return self.flowers

# Метод для вывода на экран названия цветов в отсортированном букете
    @decorator
    def print_sorted_flowers(self, parameter):
        print(f'Sorted BY {parameter}')
        for flower in self.sort_flowers(parameter):
            print(f'Flower: {flower.name}, Color: {flower.color}')

# Метод для поиска цветов в букете по среднему времени жизни
    @decorator
    def search_flowers(self, freshness):
        for flower in self.flowers:
            if flower.freshness == freshness:
                return (f'Flower with freshness {freshness} days: {flower.name}, Color: {flower.color}, '
                        f'Price: {flower.price}$')
        return f'No flowers with freshness {freshness} days'

    def __str__(self):
        return f'Bouquet: {self.flowers}'

    def __repr__(self):
        return f'Bouquet: {self.flowers}'


rose_red = Rose('Rose', 'Red', 10, 5, 15)
rose_white = Rose('Rose', 'White', 15, 2, 10)
tulip_yellow = Tulip('Tulip', 'Yellow', 5, 4, 10, 'Tiger')
tulip_red = Tulip('Tulip', 'Red', 7, 3, 12, 'Amidst')
lily_white = Lily('Lily', 'White', 20, 7, 20, 'Casablanca')
lily_pink = Lily('Lily', 'Pink', 25, 1, 25, 'Stargazer')
print(rose_red, rose_white, tulip_red, tulip_yellow, lily_white, lily_pink, sep='\n')

bouquet1 = Bouquet()
bouquet1.add_flower(rose_red)
bouquet1.add_flower(rose_white)
bouquet1.add_flower(tulip_red)
bouquet1.add_flower(tulip_yellow)
bouquet1.add_flower(lily_white)
bouquet1.print_flower_names_in_bouquet()
print(bouquet1.bouquet_price())
print(bouquet1.fading_time())

bouquet1.print_sorted_flowers('freshness')
bouquet1.print_sorted_flowers('price')
bouquet1.print_sorted_flowers('stem_length')
bouquet1.print_sorted_flowers('color')

print(bouquet1.search_flowers(4))

a = bouquet1.sort_flowers('freshness')
print(a)
