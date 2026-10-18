from admin import Admin

def main():
    ch = 0
    while ch != 2:
        print("""Please select option :)
        1. Login
        2. Exit""")
        ch = input('Enter choice: ')
        if ch == '1':
            login()
        elif ch == '2':
            print('Thank you for choosing us...')
            break
        else:
            print('Invalid choice!...')

def login():
    print('------------LOGIN PAGE------------')
    uname = 'admin'
    pword = '12345'
    user = input('Enter user name: ')
    passw = input('Enter password: ')
    if (uname == user and pword == passw):
        print('Logged in successfull...!')
        a = Admin()
    else:
        print('Invalid credentials!...')

if __name__ == '__main__':
    main()
