#!/usr/bin/python3
while True:
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
  elif option == 2:
    print('we have many museums in Rwanda, each holding many cherishable and unique History of Our Country \n \n')
    print('1.Rwanda Art Museum Situated in Nyanza, this museum showcases traditional and contemporary Rwandan art, including paintings, sculptures, and crafts \n')
    print("2.Ethnographic Museum (formerly Butare Museum): Located in Huye (formerly Butare), this museum provides insights into Rwanda's cultural history, traditional art, and lifestyle \n")
    print('3.Campaign Against Genocide Museum: Found in Kigali, this museum documents the history leading up to the 1994 genocide and the efforts to prevent and stop it. \n')
    print('4.Rwanda National Police Museum: Located in Kigali, this museum focuses on the history and activities of the Rwandan National Police. \n')
    print('5.Kigali Genocide Memorial Centre: Located in the capital city, Kigali, this memorial center is dedicated to the memory of the victims of the 1994 Rwandan Genocide. It includes exhibitions, memorials, and educational programs. \n')
    print('6.Kandt House Museum: located in Kigali examining life in Rwanda before, during and after the colonial period. \n')
    break