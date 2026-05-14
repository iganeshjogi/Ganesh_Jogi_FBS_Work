#Program to find quotient and remainder of two numbers.

dividend = int(input('Enter the Dividend:'))
divisor = int(input('Enter the divisor:'))

quotient = dividend // divisor
remainder = dividend % divisor

print(f'The quotient is {quotient} and remainder is {remainder}.')