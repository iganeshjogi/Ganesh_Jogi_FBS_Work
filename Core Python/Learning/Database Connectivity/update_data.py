import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'fbs'
)

sql = 'update employee set salary = 45000 where id = 102'

cursor = conn.cursor()
cursor.execute(sql)

conn.commit()
print('Query ok')