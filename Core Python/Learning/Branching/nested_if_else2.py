# Program to classify number ranges using nested if else

num = int(input('Enter the number: '))

if num > 0:
    if num <= 50:
        print('The number is between 1 to 50.')
    else:
        if num <= 100:
            print('The number is between 51 to 100.')
        else:
            if num <= 200:
                print('The number is between 101 to 200.')
            else:
                print('The number is grater than 200.')
else:
    print('The number is less than zero.')