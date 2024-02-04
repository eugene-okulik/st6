# while True:
#     user_num = int(input('Enter number from 1 to  15: '))
#     if user_num==15:
#         print('That is the number!')
#         break
#     print('Wrong! Try again!')   

while(user_value := int(input('Guess a number from 1 to  15: ')) !=15):
    print('Wrong! Try again!')
print('That\'s the number!')
                