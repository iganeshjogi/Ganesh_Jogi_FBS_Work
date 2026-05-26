#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

side1 = float(input('Enter the side 1 of a triangle. '))
side2 = float(input('Enter the side 2 of a triangle. '))
side3 = float(input('Enter the side 3 of a triangle. '))

# for equilateral triangle.
if side1 == side2 == side3:
    print('The triangle is equilatteral')

# for isosceles triangle.
elif side1 == side2  or side1 == side3 or side2 == side3:
    print('The trianlgle is isosceles')

# for scalene triangle.
elif side1 != side2 and side1 != side3 and side2 != side3:
    print('The triagnle is scalene ')