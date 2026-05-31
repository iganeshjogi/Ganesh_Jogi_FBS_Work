'''1. Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.'''


user = 'admin'
password = '12345'


for i in range (1, 4):
    userid= input('Enter the user id: ')
    userpass = input('Enter the password: ')
    if userid == user and userpass == password:
        print('Logged in')
        break
        print('Logged in')
    else:
        print('invalid credentials \nTry again')
else:
    print('Too many attempts \n Try again later...')