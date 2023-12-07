#!/usr/bin/python3
from connect import TourismApp, lesly


def home():
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
      print(
        '1. Akagera National Park located in Eastern Province of Rwanda, It is home to many animals such as: lions, elephants, buffaloes, leopards, and rhinos[1.8796° S, 30.7040° E] \n')
      print(
        '2.Nyungwe National Park located in Southern Province of Rwanda, It is home to many species of birds and ton of chimps.[2.5282° S, 29.2784° E]\n')
      print(
        '3.Volcanoes National Park found in Northern Province is home to the mountain gorillas, which are one of the most endangered animals in the world,It has several trails leading to the top of Mount Karisimbi, the highest volcano in Rwanda [01°28′03″S 29°29′33″E] \n')
      break
    elif option == 2:
      print('we have many museums in Rwanda, each holding many cherishable and unique History of Our Country \n \n')
      print(
        '1.Rwanda Art Museum Situated in Nyanza, this museum showcases traditional and contemporary Rwandan art, including paintings, sculptures, and crafts [-1.97529 S,30.17302° E] \n')
      print(
        "2.Ethnographic Museum (formerly Butare Museum): Located in Huye (formerly Butare), this museum provides insights into Rwanda's cultural history, traditional art, and lifestyle [48.2051° N, 16.3635° E]\n")
      print(
        '3.Campaign Against Genocide Museum: Found in Kigali, this museum documents the history leading up to the 1994 genocide and the efforts to prevent and stop it. [1.9524° S, 30.0989° E]\n')
      print(
        '4.Rwanda National Police Museum: Located in Kigali, this museum focuses on the history and activities of the Rwandan National Police. [-1.93927° S,30.05153° E] \n')
      print(
        '5.Kigali Genocide Memorial Centre: Located in the capital city, Kigali, this memorial center is dedicated to the memory of the victims of the 1994 Rwandan Genocide. It includes exhibitions, memorials, and educational programs. \n')
      print(
        '6.Kandt House Museum: located in Kigali examining life in Rwanda before, during and after the colonial period.[-1.94668° S,30.05353° E ] \n')
      break
    elif option == 3:
      hotel = int(input('What hotel do you prefer \n 1.5-star Hotel \n 2.4-star Hotel \n 3.3-star Hotel \n'))

      if (hotel > 3 or hotel < 1 or type(option) != int):
        print('Choose a number from 1 to 3')
        continue

      elif hotel == 1:
        print(
          '1.Raddison Blu Hotel and Convention Centre, located in Kigali and food there is top quality plus their stuff is friendly. \n')
        print(
          '2.Marriot Hotel, It is located in Kigali and it offer exceptinal sercives, you can find here comfartable rooms,and the pool is nice. \n')
        print(
          '3.Kigali Serena Hotel, it is found on an enchanting boulevard in the heart of Kigali in a secure location. \n')
        break

      elif hotel == 2:
        print('1.Ubumwe Grande Hotel, It is found in kigali and has stunning views. \n')
        print('2.The Retreat is a luxury, boutique hotel in the Kiyovu district of Kigali, Rwanda’s capital city. \n')
        print('3.Hotel des Mille collines has a fantastic location in the heart of Kigali. \n')
        break

      elif hotel == 3:
        print(
          "1.Amata n'Ubuki Boutique Hotel is  perfect for a romantic weekend, a business trip or to taste the many flavours of their restaurant. \n")
        print('2.Hotel Chez Lando, It is found in kigali and has stunning views. \n')
        break


def register():  # insert
    print("\n ***************** Create account *******************")
    username = input("Enter Your User Name: ")
    email = input("Enter Your User Email: ")
    password = input("Enter password: ")
    data = (username, email, password)
    sql = "INSERT INTO `users`(`Email`, `Username`, `password`) VALUES (%s,%s,%s)"
    TourismApp.execute(sql, data)
    lesly.commit()
    # end insert data
    if TourismApp.rowcount > 0:
        login()
    else:
        print("not register")
        register()


def login():  # selecet
    print("\n *********** login here ********")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    data = (username, password)
    sql = "SELECT * FROM `users` WHERE Username=%s AND password= %s"
    TourismApp.execute(sql, data)
    res = TourismApp.fetchall()
    if len(res) > 0:
        home()
    else:
        print("username and password do not match or account don't exist")
        login()


def main():
    print("welcome to our app")
    print("1 Create new account")
    print("2 Login")
    print("3 Exit")
    choice = input("enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
    else:
        print("invalid choice")
        main()

main()

