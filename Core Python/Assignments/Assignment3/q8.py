'''Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)'''

import random

user = 'admin'
password = '12345'
userid = input('Enter the user id: ')
passkey = input('Enter the password: ')

if userid == user and passkey == password:
    captcha = random.randint(1000,9999)
    print(f'Enter captcha: {captcha}')
    user_captcha = int(input('Enter the captcha:'))
    if user_captcha == captcha :
        print('Logged in successfully.')
    else:
        print('Invalid Captcha.')
    
else:
    print('Invalid credentials.')