''' 
Q1. Create a class Book with members as bid,bname,price and author.
    Add following methods:
    a. Constructor (Support both parameterized and parameterless)
    b. Destructor
    c. ShowBook
    d. Add static variable count and also maintain count of objects created. '''

class Book:

    count = 0
    
    def __init__(self, bid = 0, bname = '', price = 0, author = ''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        Book.count += 1

    def showBook(self):
        print(f'''
    Book ID   : {self.bid}
    Book Name : {self.bname}
    Price     : {self.price}
    Author    : {self.author}
    ''')
        
    def __del__(self):
        print('Book object destroyed.')


b1 = Book()
b2 = Book()
b3 = Book()

b1.showBook()

b2.showBook()

b3.showBook()

print("Total Books Created :", Book.count)