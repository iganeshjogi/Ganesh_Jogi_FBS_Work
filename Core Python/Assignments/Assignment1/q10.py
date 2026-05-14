#Write a program to calculate area of an equilateral triangle.

side = float(input('Enter the length of one side:'))

area = (3 ** 0.5 / 4) * side**2

print(f'The area of equilateral triangle having side length {side} is {area}')