from homework.alex_serebryansky.homework11.Flowers import Flowers


class Rose(Flowers):
    def __init__(self, name: str, color: str, price: int, life_time: int, stem_length: int = None):
        super().__init__(name, color, price, life_time)
        self.stem_length = stem_length

    def __str__(self):
        return (f"Flower: {self.name}, Color: {self.color}, Price: {self.price}, "
                f"Lifetime: {self.lifetime} days, Stem Length: {self.stem_length}")
