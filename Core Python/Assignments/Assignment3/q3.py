#Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 = float(input('Enter 1st angle of triangle: '))
angle2 = float(input('Enter 2nd angle of triangle: '))
angle3 = float(input('Enter 3rd angle of triangle: '))

total = angle1 + angle2 + angle3

if total == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print('The triangle is valid.')

else:
    print('The triangle is not valid.')