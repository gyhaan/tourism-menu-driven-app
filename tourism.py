#!/usr/bin/python3
print('Welcome to Rwanda, the country of thousand hills. \n')
option = int(
    input(
        'Where would like to visit \n 1.Game Parks \n 2.Museums \n 3.Hotels \n'
    ))
if (option > 3 or option < 1 or type(option) != int):
    print('Choose a number from 1 to 3')
    continue
  elif option == 1:
    print('We have a lot of National parks in Rwanda and each has its own variety of animals \n\n')
    print('1. Akagera National Park located in Eastern Province of Rwanda, It is home to many animals such as: lions, elephants, buffaloes, leopards, and rhinos \n')

    print('2.Nyungwe National Park located in Southern Province of Rwanda, It is home to many species of birds and ton of chimps.\n')

  print('3.Volcanoes National Park found in Northern Province is home to the mountain gorillas, which are one of the most endangered animals in the world,It has several trails leading to the top of Mount Karisimbi, the highest volcano in Rwanda ')
  break
