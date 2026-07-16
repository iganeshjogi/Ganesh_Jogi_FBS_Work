''' 
Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).
    Add following methods:
    a. Constructor (Support both parameterized and parameterless)
    b. Destructor
    c. ShowShirt '''


class Shirt:

    def __init__(self, sid = 0, sname = '', stype = '', price = 0, size = ''):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def showShirt(self):
        print(f'''
    Shirt ID   : {self.sid}
    Shirt Name : {self.sname}
    Shirt Type : {self.stype}
    Shirt Price: {self.price}
    Shirt Size : {self.size}
    ''')

    def __del__(self):
        print('Shirt object destroyed.')


s1 = Shirt(101, 'Polo', 'Casual', 999, 'Medium')
s2 = Shirt()

s1.showShirt()
s2.showShirt()