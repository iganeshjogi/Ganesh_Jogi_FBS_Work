#WAP to calculate area of triangle and rectangle

#1. Triangle 
height = float(input('Enter the height of triangle:'))
base = float(input('Enter the base of triangle:'))

triangle_area = 1 / 2 * height * base

print(f'The area of triangle is {triangle_area} square unit.')
#2. Rectangle
length = float(input('Enter the length of rectangle side:'))
width = float(input('Enter the width of rectangle side:'))

rectangle_area = length * width

print(f'area of rectangle is {rectangle_area} square unit.')
print(f' So the area of triangle is {triangle_area} square unit and area of rectangle is {rectangle_area} square unit.')