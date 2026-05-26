#Write a program to check if the given number is positive or negative.

number = int(input('Enter the number: '))

if number == 0:
    print('The number is neutral.')
elif number > 0:
    print('The number is positive.')
elif number < 0:
    print('The number is negative.')