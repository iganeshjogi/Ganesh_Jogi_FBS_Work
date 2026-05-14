#Find the sum of three-digit number.

number = int(input('Enter the three digit number:'))

third_digit = number % 10
second_digit = number // 10
second_digit = second_digit % 10
first_digit = number // 100

digit_sum = first_digit + second_digit + third_digit

print(f'The sum of digit {number} is {digit_sum}.')
