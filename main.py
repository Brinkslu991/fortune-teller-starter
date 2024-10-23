# Lucas Brinks
# 10/23/24
# Fortune Teller

import time
import random
import sys

fortunes = ['You\'re a winner!', 'A secret admirer will soon send you a sign of affection!', 'The one you love is much closer than you think!', 'Good things will happen to you by the end of the day today!', 'Fame and fortune will be yours if you take the time to learn Python!', 'I\'m just a computer program, and have no magical powers!', 'It ends today', 'The Rapture has begun', 'Play Cookie Clicker', 'Do you know what Pneumonoultramicroscopicsilicovolcanoconiosis is']

magic_colors = ['blue', 'red', 'green', 'yellow']

user_name = input('Please enter your name: ')
user_name = user_name.title()
print(f'Hey there {user_name}, welcome to my python Fortune Teller program.')

question1 = input('Would you like to know what you future holds?: ')
question1 = question1.lower()
time.sleep(1)

if question1 in ['y', 'yes', 'sure', 'ye', 'yes please']:
    time.sleep(1)
    print(f'Okay! To get your fortune, please input a magic color: {magic_colors}')
    color = input('Enter one of the colors listed above: ')
    color = color.lower()
    time.sleep(1)
    print('Getting your fortune...')
    time.sleep(1)
    print(f'Here is your fortune, {user_name}')

    if color in magic_colors:
        index = random.randint(0, len(fortunes)-1)
        print(fortunes[index])
    else:
        print(f'Please choose one of the colors from the list: {magic_colors}')
        time.sleep(1)
        print('Once you have input a magic color, I will reveal your fortune!')
else:
    print(f'Thank you for playing my Fortune Teller game today, {user_name}!')
    print('Goodbye')
    sys.exit()

print(f'Thank you for playing my Fortune Teller game today, {user_name}!')
print('Goodbye')
