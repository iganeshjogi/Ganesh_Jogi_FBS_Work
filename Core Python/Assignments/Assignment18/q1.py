'''
Q1. Create a class Complex Number with data members as real and imag and add
following methods :
    a. Constructor
    b. Destructor
    c. Overload +,- operator'''

class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print("Complex Number Object Destroyed")

    def __add__(self,other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real,imag)
    
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real,imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

c1 = ComplexNumber(10, 3)
c2 = ComplexNumber(5, 1)

c3 = c1 + c2
c4 = c1 - c2

print(c3)
print(c4)