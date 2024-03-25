from homework.alex_serebryansky.homework11.Bouquet import Bouquet
from homework.alex_serebryansky.homework11.Flowers import Flowers
from homework.alex_serebryansky.homework11.Rose import Rose

white_rose = Rose('Rose', 'White', 10, 5, 150)
red_rose = Rose('Rose', 'Red', 12, 6, 160)
white_tulip = Flowers('Tulip', 'White', 5, 4)
violet_tulip = Flowers('Tulip', 'Violet', 4, 3)
white_chamomile = Flowers('Chamomile', 'White', 7, 7)
yellow_chamomile = Flowers('Chamomile', 'Yellow', 9, 10)


birthdays_bouquet = Bouquet()
birthdays_bouquet.add_flower(red_rose)
birthdays_bouquet.add_flower(white_rose)
birthdays_bouquet.add_flower(red_rose)
birthdays_bouquet.add_flower(white_rose)
birthdays_bouquet.add_flower(red_rose)

wifes_bouquet = Bouquet()
wifes_bouquet.add_flower(violet_tulip)
wifes_bouquet.add_flower(white_chamomile)
wifes_bouquet.add_flower(red_rose)
wifes_bouquet.add_flower(white_tulip)
wifes_bouquet.add_flower(yellow_chamomile)

birthdays_bouquet.print_bouquet()
birthdays_bouquet.sort_flowers_by('price')
birthdays_bouquet.print_bouquet()
birthdays_bouquet.search_flowers(4, 5)
wifes_bouquet.print_bouquet()
wifes_bouquet.sort_flowers_by('color')
wifes_bouquet.print_bouquet()
