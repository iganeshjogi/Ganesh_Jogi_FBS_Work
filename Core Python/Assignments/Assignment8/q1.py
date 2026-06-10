# 1. Write a program to calculate area of rectangle

def rectangle_Area(length,width):
    return length * width 
    

rec_height = float(input('Enter the height of rectangle: '))
rec_width = float(input('Enter the width of rectangle: '))

area = rectangle_Area(rec_height,rec_width)

print(f'The area of rectangle having height {rec_height} and width {rec_width} is {area} square unit.')