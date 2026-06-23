# #1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

# s1 = float(input('Enter the marks out of 100 of subject 1: '))
# s2 = float(input('Enter the marks out of 100 of subject 2: '))
# s3 = float(input('Enter the marks out of 100 of subject 3: '))
# s4 = float(input('Enter the marks out of 100 of subject 4: '))
# s5 = float(input('Enter the marks out of 100 of subject 5: '))

# total = s1 + s2 + s3 + s4 + s5
# percent = total / 500 * 100
# print(f'The percentage of sudent is {percent} %')

# #2. Write a program to calculate area of rectangle based on length and breadth.

# l = float(input('Enter the length of a rectangle: '))
# b = float(input('Enter the breadth of a rectangle: '))

# area = l * w
# print(f'The area of rectangle is {area} square unit.')

# #3. Program to find quotient and remainder of two numbers.

# d1 = int(input('Enter the dividend: '))
# d2 = int(input('Enter the divisor: '))

# q = d1 // d2
# r = d1 % d2 

# print(f'The quotient and remainder of {d1} after division by {d2} is {q} and {r} respectively.')

# #4. Write a program to enter P, T, R and calculate simple Interest.

# p = float(input('Enter the principle amount: '))
# t = float(input('Enter the number of years: '))
# r = float(input('Enter the rate of interest: '))

# si = p * t * r / 100
# print(f'The simple interest is {si} rs.')

# #5. Write a program to enter P, T, R and calculate Compound Interest.

# p = float(input('Enter the principle amount: '))
# t = float(input('Enter the number of years: '))
# r = float(input('Enter the rate of interest: '))

# ci = p * (1 + r /100)**t - p
# print(f'The compound interest is {ci} rs.')

# #6. Write a Program to input two angles from user and find third angle of the triangle.

# ang1 = float(input('Enter the first angle of triangle: '))
# ang2 = float(input('Enter the second angle of triangle: '))

# ang3 = 180 - (ang1 + ang2 )
# print(f'The third angle of a triangle is {ang3} degree.')

# #7. Program to Find the Roots of a Quadratic Equation

# a = float(input('Enter the value of a: '))
# b = float(input('Enter the value of b: '))
# c = float(input('Enter the value of c: '))

# d = b**2 - 4 * a * c

# root1 = (-b + d**0.5) / (2 * a)
# root2 = (-b - d**0.5) / (2 * a)

# print(f'The roots of quadratic equation are {root1} and {root2}.')

# #8. Write a program to convert days into years, weeks and days.

# n = int(input('Enter the days: '))

# years = n // 365
# n= n % 365
# weeks = n // 7
# days = n % 7


# print(f'{n} days are equal to {years} year, {weeks} week, {days} days.')

# #9. Write a program to enter base and height of a triangle and find its area.

# height = float(input('Enter the height:'))
# base = float(input('Enter the base: '))

# area = 1 / 2 * height * base
# print(f'The area of triangle is {area} square unit')

# #10. Write a program to calculate area of an equilateral triangle.

# side = float(input('Enter the side of a triangle: '))

# area = (3**0.5 / 4) * side**2

# print(f'The area of equilateral number is {area:.2f}.')

# #11. Find the area and circumference of circle.

# radius = float(input('Enter the radius: '))

# circumference = 2 * 3.14 * radius
# area = 3.14 * radius**2
# print(f'The circumference of a circle is {circumference} unit and area is {area} square unit.')

# #12. Find the volume of sphere.
# radius = float(input('Enter the radius: '))

# volume =  (4 / 3) * 3.14 * radius ** 3
# print(f'The volume of sphere is {volume:.2f} cubic unit.')

'Assignment2'
# #1. Convert the time entered in hh,min and sec into seconds.

# hh = int(input('Enter the Hour: '))
# min  = int(input('Enter the minutes: '))
# sec = int(input('Enter the seconds: '))

# h = hh * 3600
# m = min * 60
# total_sec = h + m + sec

# print(f'The total second are {total_sec}.')

# #2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# celcius = int(input('Enter the tempareture: '))
# fahrenheit = (celcius * 1.8) + 32
 
# print(f'The {celcius} celcius is equal to {fahrenheit} fahrenheit.')

# #3. Convert distant given in feet and inches into meter and centimeter.

# feet = float(input('Enter the distance feet: '))
# inches = float(input('Enter the distance inches: '))

# total_inches = (feet * 12) + inches
# centimeters = total_inches * 2.54
# meters = centimeters / 100
# print(f'The total distance is {meters} in meters and {centimeters} in centimeters.')

# #4. WAP to calculate selling price of book based on cost price and discount.
# cp = float(input('Enter the cost price: '))
# discount = float(input('Enter the discount percent: '))
# sp = cp - (cp * discount / 100) 
# print(f'The selling price of a book is {sp} rs.')

# #5. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

# salary = float(input('Enter the salary: '))
# da = salary*10/100
# ta = salary*12/100
# hra = salary*15/100

# total_salary = salary + da + ta + hra

# print(f'The total salary is {total_salary} rs.')

# #6. Find the sum of three-digit number.
# num = int(input('Enter the three digit number: '))

# d1 = num % 10
# num = num // 10
# d2 = num % 10
# num = num // 10
# d3 = num 
# sum = d1 + d2 + d3 
# print(f'The sum of digits in the number is {sum}.')

# #7. Write a program to swap two numbers using third variable.

# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# print(a,b)
# c = b
# b = a
# a = c
# print(a,b)

# #8. Write a program to swap two numbers without using third variable.
# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
# print(a,b)
# a, b = b, a
# print(a,b)

# #9.Write a program to reverse three-digit number.

# num = int(input('Enter the number: '))
# temp = num
# d1 = num % 10
# num = num // 10
# d2 = num % 10
# d3 = num // 10
# print(f'The reverse of a number {temp} is {d1}{d2}{d3}.')

# #10. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# amount = int(input('Enter the amount: '))

# pink = amount // 2000
# amount = amount % 2000 

# grey = amount // 500
# amount = amount % 500

# orange = amount // 200
# amount = amount % 200

# purple = amount // 100
# amount = amount % 100

# blue = amount // 50
# amount = amount % 50

# green = amount // 20
# amount = amount % 20

# brown = amount // 10

# minimum_notes = pink + grey + orange +purple + blue + green + brown

# print(f'The minimum number of notes required are {minimum_notes}.')