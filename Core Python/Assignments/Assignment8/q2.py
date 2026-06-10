# 2. Write a program to calculate area of circle

def circle_area(r):
    return 3.14 * r ** 2

radius = float(input('Enter the radius of a circle: '))

area = circle_area(radius)

print(f'The area of a circle having radius {radius} is {area} square unit.')