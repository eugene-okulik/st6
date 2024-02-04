insert_number = int(input('Enter the number I mean: '))
my_number = 6

while insert_number != my_number:
    print('You guessed wrong, try again')
    insert_number = int(input('Enter the number I mean: '))

print('Congratulations, you guessed the number!!!')
