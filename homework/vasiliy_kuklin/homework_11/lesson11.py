class Flowers:
    def __init__(self, freshness, color, stem_length, time_live, cost, name):
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.time_live = time_live
        self.cost = cost
        self.name = name

    def __str__(self):
        return f'{self.color}'

    def __repr__(self):
        return f'{self.color}, {self.cost}, {self.freshness}, {self.stem_length}, {self.time_live}, {self.name}'


class BeautifulFlowers(Flowers):
    def __init__(self, name, freshness, color, stem_length, time_live, cost):
        super().__init__(freshness, color, stem_length, time_live, cost, name)


class Bouquet:
    """Букет"""

    def __init__(self):
        self.list_time = []
        self.fading_time = self.fading_time
        self.flowers = []
        self.cost_flowers = []

    def fading_time(self):
        """Время увядания"""
        for i in self.flowers:
            self.list_time.append(i.time_live)
            time_dead = (sum(self.list_time) / len(self.list_time))
        return print(f'Букет завянет через  {time_dead} дней')

    def cost_determination(self):
        """Определение стоимости букета"""
        for cos in self.flowers:
            self.cost_flowers.append(cos.cost)
            sum_buket = sum(self.cost_flowers)
        return print(f'стоимость букета равна {sum_buket}')

    def bouquet_sorting_cost(self):
        """Сортировка букета по стоимости"""
        self.flowers.sort(key=lambda x: x.cost)
        return self.flowers

    def bouquet_sorting_time_live(self):
        """Сортировка букета по времени жизни"""
        self.flowers.sort(key=lambda x: x.time_live)
        return self.flowers

    def search_flower(self, time_live):
        """Поиск цветка в букете по времени жизни"""
        for i in self.flowers:
            if i.time_live == time_live:
                print(i.time_live)
            else:
                print("нет совпадений")


rose = BeautifulFlowers('rose', 1, 'red', 30, 7, 950)
ficus = BeautifulFlowers('ficus', 2, 'green', 25, 20, 250)

my_buket = Bouquet()
my_buket.flowers.append(rose)
my_buket.flowers.append(ficus)
my_buket.fading_time()
my_buket.cost_determination()

print(my_buket.bouquet_sorting_cost())
print(my_buket.bouquet_sorting_time_live())
print(my_buket.search_flower(time_live=20))
