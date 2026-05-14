#Write a program to enter P, T, R and calculate simple Interest.

p = int(input('Enter the principle amount:'))
t = int(input('Enter the time in years:'))
r = int(input('Enter the rate of interest:'))

si = p * t * r / 100

print(f'The simple interest is {si} rs.')