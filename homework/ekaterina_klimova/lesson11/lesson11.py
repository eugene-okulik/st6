class Flowers:
    def __init__(self, name, color, long, life_time, cut_days, price):
        self.name = name
        self.long = long
        self.life_time = life_time
        self.cut_days = cut_days
        self.price = price


class Rose(Flowers):
    def __init__(self, color, long, life_time, cut_days, price):
        super().__init__("Роза", color, long, life_time, cut_days, price)


class Camomile(Flowers):
    def __init__(self, color, long, life_time, cut_days, price):
        super().__init__("Ромашка", color, long, life_time, cut_days,price)


class Tulip(Flowers):
    def __init__(self, color, long, life_time, cut_days, price):
        super().__init__("Тюльпан", color, long, life_time, cut_days, price)

class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)  

    def calculate_bouquet_cost(self):
        total_cost = 0       
        for flower in self.bouquet:
            rest_life = (flower.life_time - flower.cut_days) / flower.life_time
            if flower.long == "long":
                k = 1.5
            elif flower.long == "middle":
                k = 1    
            elif flower.long == "short":
                k = 0.5
            total_cost += flower.price * rest_life * k
        return total_cost

    # определяет время его увядания по среднему времени жизни всех цветов в букете.
    def wilted_the_bouquet(self):
        freshness = 0
        for flower in self.bouquet:
            freshness += (flower.life_time - flower.cut_days)
        return freshness / len(self.bouquet)

    def sort_flowers_by_freshness(self):
        self.bouquet.sort(key=lambda x: x.cut_days)

    def sort_flowers_by_price(self):
        self.bouquet.sort(key=lambda x: x.price)

    def sort_flowers_by_life_time(self):
        self.bouquet.sort(key=lambda x: x.life_time)

    def search_by_life_time(self, target_freshness):
        found_flowers = []
        for flower in self.bouquet:
            if flower.life_time == target_freshness:
                found_flowers.append(flower)
        return found_flowers



red_rose = Rose("красный", "short", 10, 3, 7)
white_camomile = Camomile("белый", "middle", 14, 1, 5)
pink_rose = Rose("розовый", "long", 10, 1, 9)
black_tulip = Tulip("черный", "middle", 8, 1, 5)

bouquet = Bouquet()
bouquet.add_flower(red_rose)
bouquet.add_flower(white_camomile)
bouquet.add_flower(pink_rose)
bouquet.add_flower(black_tulip)

#Информация о букете
print(f'Средняя свежесть букета: {bouquet.wilted_the_bouquet()}')
print(f'Стоимость букета: {bouquet.calculate_bouquet_cost()}')

#сортировки по свежести/цене/времени жизни
bouquet.sort_flowers_by_freshness()
print("Цветы в букете отсортированы по свежести:")
for f in bouquet.bouquet:
    print(f.name, f.cut_days)

bouquet.sort_flowers_by_price()
print("Цветы в букете отсортированы по стоимости:")
for f in bouquet.bouquet:
    print(f.name, f.price)

bouquet.sort_flowers_by_life_time()
print("Цветы в букете отсортированы по времени жизни:")
for f in bouquet.bouquet:
    print(f.name, f.life_time)

#Поиск цветка по времени жизни
l_time = int(input("Введите необходимое время жизни цветка: "))
found_flowers = bouquet.search_by_life_time(l_time)
print(f'цветы со свежестью {l_time}:')
for f in found_flowers:
    print(f.name, f.cut_days)
