import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Password',
    database = 'fbs'
)

# Parameterless
# sql = f'insert into employee values(101, "Ganesh", 50000)'

# Parameterized
sql = 'insert into employee values(%s, %s, %s)'
values = (102, 'Amit', 40000)

cursor = conn.cursor()
cursor.execute(sql, values)
conn.commit()
print('Query executed successfully.')