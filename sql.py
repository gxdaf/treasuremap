import mysql.connector
import a

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456"
  database = "treasuremap"
)

cursor = db.cursor()

#cursor.execute('CREATE DATABASE treasuremap')


print(db)