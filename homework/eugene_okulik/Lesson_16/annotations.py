from typing import Literal, List


def calc(x: int, y: int) -> int:
    result = x * y
    return result


calc_result = calc(1, 3)
# print(calc_result + 'a')


class Flowers:
    def __init__(self, price, color):
        self.price = price
        self.color = color


rose = Flowers(12, 'white')
tulip = Flowers(5, 'yellow')


def print_lowers_price(cvetok: Flowers):
    print(cvetok.price)


def hi_or_bye(word: Literal['hi', 'bye']):
    match word:
        case 'hi':
            print('HELLO')
        case 'bye':
            print('GOOD BYE')
        case _:
            print()


hi_or_bye('hi')


def sum_all(integers: List[int]):
    return sum(integers)


sum_all([1, 3])
