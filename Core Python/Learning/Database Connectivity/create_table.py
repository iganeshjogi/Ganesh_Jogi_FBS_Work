import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password',
    database = 'fbs'
)

sql = 'create table employee(id int, name varchar(30), salary int)'


cursor = conn.cursor()
cursor.execute(sql)
print('Query executed successfully.')