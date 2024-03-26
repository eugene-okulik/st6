class Flowers:
    def __init__(self, name: str, color: str, price: int, lifetime: int):
        self.name = name
        self.color = color
        self.price = price
        self.lifetime = lifetime

    def __str__(self):
        return f"Flower: {self.name}, Color: {self.color}, Price: {self.price}, Lifetime: {self.lifetime} days"
