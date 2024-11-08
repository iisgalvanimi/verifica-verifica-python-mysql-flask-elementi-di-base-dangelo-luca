import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("USE Animali")
mycursor.execute("CREATE TABLE IF NOT EXISTS Uccelli (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Comune VARCHAR(50),famiglia VARCHAR(50),Apertura_Alare INT, Habitat VARCHAR(50),Alimentazione VARCHAR(50))")