#program to check login credentials are valid or in valid

user = 'ADMIN'
password = '12345'

userid = input('Enter the userid:')
passkey = input('Enter the passkay:')

if userid == 'ADMIN' and passkey == '12345':
    print('Logged in successfully.')

else:
    print('Invalid credentials.')