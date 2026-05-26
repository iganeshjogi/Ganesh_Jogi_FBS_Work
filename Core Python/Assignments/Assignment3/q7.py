#Write a program to check if user has entered correct userid and password.

user = 'ADMIN'
password = '12345'

userid = input('Enter the user id: ')
passkey = input('Enter the password: ')

if userid == user and passkey == password:
    print('Logged in successfully.')
    
else:
    print('Invalid credentials.')