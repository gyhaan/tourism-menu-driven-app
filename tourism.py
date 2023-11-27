#!/usr/bin/python3
print('Welcome to Rwanda, the country of thousand hills. \n')
option = int(
    input(
        'Where would like to visit \n 1.Game Parks \n 2.Museums \n 3.Hotels \n'
    ))
if (option > 3 or option < 1 or type(option) != int):
  raise ValueError('Please Choose a number from 1 to 3')
elif type(option) != int:
  raise TypeError('Use numbers only')
