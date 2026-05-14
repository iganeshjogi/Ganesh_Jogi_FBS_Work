#Write a program to enter P, T, R and calculate Compound Interest.

p = int(input('Enter the principle amount:'))
t = int(input('Enter the time in years:'))
r = int(input('Enter the rate of interest:'))

ci =  p * (1 + r / 100)**t - p

print(f'The compound interest is {ci} rs.')