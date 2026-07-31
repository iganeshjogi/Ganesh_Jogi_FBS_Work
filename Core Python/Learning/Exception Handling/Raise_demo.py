from user_defined_exception import UserDefinedException, NameException, MobileException

age = int(input('Enter age: '))

if (age > 0 and age <= 120):
    print('Age is', age)

else:
    # raise f'Error: Age is not valid.'   # TypeError: exceptions must derive from BaseException
    raise UserDefinedException(age)

name = input('Enter Name: ')


if all(ch.isalpha() or ch.isspace() for ch in name):
    print('Name is',name)

else:
    raise NameException(name)

mobile_no = input('Enter Mobile Number: ')

if (mobile_no.isdigit() and len(mobile_no) == 10 and mobile_no[0] in '6789'):
    print('Mobile Number is',mobile_no) 

else:
    raise MobileException(mobile_no)