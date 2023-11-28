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
  elif option == 3:
    print('We have many luxurious hotels in Rwanda, All five stars hotels with affordable and good customercare services. \n\n')
    print('1.Raddison Blu Hotel and Convention Centre, located in Kigali and food there is top quality plus their stuff is friendly. \n')
    print('2.Marriot Hotel, It is located in Kigali and it offer exceptinal sercives, you can find here comfartable rooms,and the pool is nice. \n')
    print('3.Kigali Serena Hotel, it is found on an enchanting boulevard in the heart of Kigali in a secure location. \n')
    print('4.Ubumwe Grande Hotel, It is found in kigali and has stunning views. \n')
    print('5.The Retreat is a luxury, boutique hotel in the Kiyovu district of Kigali, Rwanda’s capital city. \n')
    print('6.Hotel des Mille collines has a fantastic location in the heart of Kigali. \n')
    print('7.villa Asimba is Located in Kigali, 2.9 miles from Kigali Centenary Park, Villa Asimba provides accommodations with an outdoor swimming pool,free private parking,a garden. \n')
    print("8.Grand Legacy Hotelis the closest modern accommodation to Kigali International Airport. The stylish hotel is a great addition to the up and coming suburb of Remera, and a 15 minute drive to Kigali's city center. \n")
    print("9.Amata n'Ubuki Boutique Hotel is  perfect for a romantic weekend, a business trip or to taste the many flavours of their restaurant. \n")
    print('10.High Grand Villa has spectacular views of the magical hills of Rwanda as it is situation at Rebero Mountain. \n)
    break
