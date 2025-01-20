import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a databse

cursorObject.execute("CREATE DATABASE bartex")

print('All done!')
