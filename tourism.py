#!/usr/bin/python3
print('Welcome to Rwanda, the country of thousand hills. \n')
while True:
    option = int(
        input(
            'Where would like to visit \n 1.Game Parks \n 2.Museums \n 3.Hotels \n'
        ))
    if (option > 3 or option < 1 or type(option) != int):
        print('Choose a number from 1 to 3')
        continue

