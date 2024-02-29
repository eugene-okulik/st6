import random


my_var = 42
variable_with_not_so_short_name = 'New Delhi'


def random_weather(city):
    cities = {
        'New York': [12, 14, 15, 16],
        'New Delhi': [23, 24, 25, 26, 27]
    }
    return random.choice(cities[city])


class MyClass:
    my_value = 11

    def my_method(self):
        return 'hello'
