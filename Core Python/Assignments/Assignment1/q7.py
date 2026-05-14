#Program to Find the Roots of a Quadratic Equation.

a = float(input('Enter the value of a:'))
b = float(input('Enter the value of b:'))
c = float(input('Enter the value of c:'))

d = b**2 - 4*a*c

root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)

print(f'''The first root value is {root1}
      and The second root value is {root2}''')