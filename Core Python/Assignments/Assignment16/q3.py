''' 
Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).
    Add following methods:
    a. Constructor (Support both parameterized and parameterless)
    b. Destructor
    c. ShowShirt
    d. For each size of shirt price should change by 10%.
    (eg. If size is small then price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept. '''

class Shirt:

    increment = 10

    def __init__(self, sid = 0, sname = '', stype = '', price = 0, size = ''):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def calculatePrice(self):

        final_price = self.price

        if self.size.lower() == 'small':
            final_price = 1000

        elif self.size.lower() == "medium":
            final_price += self.price * Shirt.increment / 100

        elif self.size.lower() == "large":
            final_price += self.price * (2 * Shirt.increment) / 100

        elif self.size.lower() == "xlarge":
            final_price += self.price * (3 * Shirt.increment) / 100

        return final_price


    def showShirt(self):
        print(f'''
    Shirt ID   : {self.sid}
    Shirt Name : {self.sname}
    Shirt Type : {self.stype}
    Base Price : {self.price}
    Shirt Size : {self.size}
    Final price: {self.calculatePrice()}
    ''')

    def __del__(self):
        print('Shirt object destroyed.')


s1 = Shirt(101, "Polo", "Casual", 1000, "Small")
s2 = Shirt(102, "Levis", "Formal", 1000, "Medium")
s3 = Shirt(103, "Nike", "Casual", 1000, "Large")
s4 = Shirt(104, "Allen Solly", "Formal", 1000, "XLarge")

s1.showShirt()
s2.showShirt()
s3.showShirt()
s4.showShirt()