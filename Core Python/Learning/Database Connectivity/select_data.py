import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password',
    database = 'fbs'
)

sql = 'select * from employee'

cursor = conn.cursor()
cursor.execute(sql)

res = cursor.fetchall()
# print(res)

for emp in res:
    print(emp)