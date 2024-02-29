# import random
from random import random, randint, randrange, choice
# from homework.eugene_okulik.Lesson_12 import useful
from homework.eugene_okulik.Lesson_12.useful import random_weather, MyClass
from homework.eugene_okulik.Lesson_12.useful import variable_with_not_so_short_name as vwnssn
# from homework.eugene_okulik.Lesson_12.useful import *


my_list = [1, 'text', False]
print(round(random() * 100))
print(randint(1, 2))
print(randrange(2, 50, 2))
print(choice(my_list))


res = random_weather(vwnssn)
print(res)
# print(my_var)

my_obj = MyClass()
print(my_obj.my_value)
