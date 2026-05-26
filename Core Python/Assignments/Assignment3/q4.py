#Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1 = float(input('Enter the side1 of a triangle. '))
side2 = float(input('Enter the side2 of a triangle. '))
side3 = float(input('Enter the side3 of a triangle. '))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('The triangle is valid.')

else:
    print('The triangle is not valid.')