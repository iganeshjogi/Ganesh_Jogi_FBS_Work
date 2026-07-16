''' 
Q1. Create a class Book with members as bid,bname,price and author.
    Add following methods:
    a. Constructor (Support both parameterized and parameterless)
    b. Destructor
    c. ShowBook '''


class Book:

    def __init__(self, bid = 0, bname = '', price = 0, author = ''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showBook(self):
        print(f'''
    Book ID   : {self.bid}
    Book Name : {self.bname}
    Price     : {self.price}
    Author    : {self.author}
    ''')
        

    def __del__(self):
        print('Book object destroyed.')


b1 = Book(101, 'Game of Thrones', 150, 'G.G.Martin')
b2 = Book()

b1.showBook()
b2.showBook()