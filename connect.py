# import mysql connnector
import mysql.connector

# create Database Connection

lesly = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tourism_app")

TourismApp = lesly.cursor()
