class UserDefinedException(Exception):
    def __init__(self, age):
        self.age = age
  
    def __str__(self):
        return f'{self.age} is not valid age.'
    
class NameException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is not valid name.'
    
class MobileException(Exception):

    def __init__(self, mobile_no):
        self.mobile_no = mobile_no

    def __str__(self):
        return f'{self.mobile_no} is not valid mobile number.'