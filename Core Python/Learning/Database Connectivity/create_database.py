import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password'
)

sql = 'create database fbs'


cursor = conn.cursor()
cursor.execute(sql) 
print('Query executed successfully.')