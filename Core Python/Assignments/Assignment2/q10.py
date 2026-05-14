#Write a program to reverse three-digit number.

number = int(input('Enter the three digit number:'))

third_digit = number % 10
first_digit = number // 100
second_digit = number // 10
second_digit = second_digit % 10


print(f'The reverse of three digit number {number} is {third_digit}{second_digit}{first_digit}')