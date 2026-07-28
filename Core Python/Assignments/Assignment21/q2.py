'''
2. Create class television that has members to hold the model number ,screen size
and price. Take a member function to take input from user, If more than 4 digits
are entered for model number, if screen size is smaller than 12 inches or greater
than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
exception.
Write a main() that instantiates an object and allows the user to enter and display
data. If exception is caught, replace all data member values with zero '''

class Television:

    def __init__(self, model_number=0, screen_size=0, price=0) :
        self.model_number = model_number
        self.screen_size = screen_size
        self.price = price

    def accept(self):
        self.model_number = int(input('Enter the model number: '))

        if len(str(self.model_number)) > 4:
            raise Exception('Model Number should be not more than 4 numbers')

        self.screen_size = int(input('Enter the size of screen: '))

        if self.screen_size < 12 or self.screen_size > 70:
            raise Exception('Screen size should be between 12 and 70 inches.')

        self.price = int(input('Enter the price of Television: '))

        if self.price < 0 or self.price > 5000:
            raise Exception('Price should be between ₹0 and ₹5000.')

    def display(self):
        print(f'''
        Model Number : {self.model_number}
        Screen Size  : {self.screen_size}
        Price        : {self.price} ''')

tv = Television()

try:
    tv.accept()
    tv.display()

except Exception as e:
    print(e)

    tv = Television()

    tv.display()