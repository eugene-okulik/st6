import math
from typing import Literal


class Bouquet:
    def __init__(self):
        self.bouquet = []
        self.bouquet_price = None
        self.dead_time = None

    def add_flower(self, flower):
        self.bouquet.append(flower)
        self.bouquet_price = sum([flower.price for flower in self.bouquet])
        dead_times = [flower.lifetime for flower in self.bouquet]
        self.dead_time = math.floor(sum(dead_times) / len(dead_times))

    def sort_flowers_by(self, sort_param: Literal['color', 'price', 'lifetime']):
        if sort_param == 'color':
            self.bouquet.sort(key=lambda item: item.color)
        elif sort_param == 'price':
            self.bouquet.sort(key=lambda item: item.price)
        elif sort_param == 'lifetime':
            self.bouquet.sort(key=lambda item: item.lifetime)
        else:
            print('Invalid sort')
        return self.bouquet

    def search_flowers(self, min_lifetime: int, max_lifetime: int):
        flowers_between_lifetime = []
        for flower in self.bouquet:
            if min_lifetime <= flower.lifetime <= max_lifetime:
                flowers_between_lifetime.append(flower)
        for flower in flowers_between_lifetime:
            print(flower)

    def print_bouquet(self):
        for flower in self.bouquet:
            print(flower, sep=' ')
        print(f'bouquet price is {self.bouquet_price}$, bouquet time is {self.dead_time} days')
