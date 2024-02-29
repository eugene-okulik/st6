class Flower:
    def __init__(self, name, color, height, price, life_time):
        self.name = name
        self.color = color
        self.height = height
        self.price = price
        self.life_time = life_time

    def __repr__(self):
        return f"(Name: {self.name}  Price: {self.price} Color: {self.color} Height: {self.height})"


class Rose(Flower):
    def __init__(self, name, color, height, price, life_time, number_of_petals):
        super().__init__(name, color, height, price, life_time)
        self.number_of_petals = number_of_petals


class Tulip(Flower):
    def __init__(self, name, color, height, price, life_time, aroma):
        super().__init__(name, color, height, price, life_time)
        self.aroma = aroma


class Bouquet:
    def __init__(self, *args):
        self.flowers = list(args)

    def total_cost(self):
        """Determining the cost of a bouquet."""
        total_price = sum(flower.price for flower in self.flowers)
        return total_price

    def fading_time(self):
        """Determining the wilting time based on the average life-time of all flowers in a bouquet."""
        find_time = [obj.life_time for obj in self.flowers]
        return sum(find_time) // len(find_time)

    def sort_by_key(self, key):
        """Sorting flowers in a bouquet according to parameters"""
        flowers_list = sorted(self.flowers, key=lambda obj: getattr(obj, key))
        print(f'Flowers sorted by {key}: {flowers_list}')

    def find_max_price(self):
        """Search for flowers in a bouquet by parameters"""
        max_flower = max(self.flowers, key=lambda x: x.price)
        print(f'Maximum flower price is: {max_flower}')

    def find_flowers_with_price_less_than(self, price_find):
        """Search for flowers in a bouquet by parameters"""
        flowers_list = []
        for obj in self.flowers:
            if obj.price < price_find:
                flowers_list.append(obj)
        for obj in flowers_list:
            print(f'Flowers with price less than {price_find}: {obj.name} - {obj.price}')


flower_1 = Flower('chamomile', 'white', 40, 45, 9)
flower_2 = Rose("rose", "red", 30, 100, 6, 10)
flower_3 = Tulip("lily", "white", 25, 77, 5, "sweet")
flower_4 = Flower("peonies", "pink", 42, 101, 6)
flower_5 = Flower("chrysanthemum", "yellow", 35, 90, 8)

flower_bouquet = Bouquet(flower_1, flower_3, flower_4, flower_5)
total_bouquet_cost = flower_bouquet.total_cost()
print(f'The total cost of the bouquet is: ${total_bouquet_cost}')
my_bouquet_fading_time = flower_bouquet.fading_time()
print(f'Time of withering according to the average lifespan:$ {my_bouquet_fading_time} days')
print('Sorting for flowers:')
flower_bouquet.sort_by_key('price')
flower_bouquet.sort_by_key('height')
flower_bouquet.sort_by_key('life_time')
print('Search for flowers:')
flower_bouquet.find_max_price()
flower_bouquet.find_flowers_with_price_less_than(price_find=60)
