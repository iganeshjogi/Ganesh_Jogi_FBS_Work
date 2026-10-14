import mysql.connector

class Datastore:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                user = 'username',
                password = 'Password',
                database = 'DB'
            )
            self.cursor = self.conn.cursor()
        
        except Exception as e:
            print('Error:', e)

    def addData(self, obj, table_name):
        if table_name == 'employee':
            sql = f'insert into employee values(%s, %s, %s, %s )'
            values = obj.toTuple()
            self.cursor.execute(sql, values)
            self.conn.commit() 

        return 'Data added Successfully.'
    
    def showAllData(self, table_name):
        sql = f'select * from {table_name}'
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def getData(self, id, table_name):
        sql = f'select * from {table_name} where id={id}'
        self.cursor.execute(sql)

        return self.cursor.fetchone()
    
    def updData(self, obj, table_name):
        if(table_name == 'employee'):
            sql = f'update {table_name} set name = %s, salary = %s, dept = %s where id = %s'
            values = (obj.name, obj.salary, obj.dept, obj.id)
        self.cursor.execute(sql, values)
        self.conn.commit()

        return 'Data updated successfully.'
    
    def delData(self, id, table_name):
        if table_name == 'employee':
            sql = f'delete from {table_name} where id = {id}'
        self.cursor.execute(sql)
        self.conn.commit()

        return 'Data deleted successfully.'    

if(__name__ == '__main__'):
    from employee import Employee