'''
Q2. Create a class Product with members as pid,pname,price and quantity.
    Add following methods:
    a. Constructor (Support both parameterized and parameterless)
    b. Destructor
    c. ShowProduct '''


class Product:

    def __init__(self, pid = 0, pname = '', price = 0, quantity = 0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print(f'''
    Product ID   : {self.pid}
    Product Name : {self.pname}
    Price        : {self.price}
    Quantity     : {self.quantity}
    ''')

    def __del__(self):
        print('Product object destroyed.')


p1 = Product(101, 'Mobile', 10000, 1)
p2 = Product()

p1.showProduct()
p2.showProduct()