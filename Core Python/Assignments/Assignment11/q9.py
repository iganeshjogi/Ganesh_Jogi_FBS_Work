# 9. Write a program to create three lists of numbers, their squares and cubes.

numbers = [1, 2, 3, 4, 5]

squares = []
cubes= []

for n in numbers:
    squares.append(n**2)
    cubes.append(n**3)
print(f'Numbers: {numbers}\nSquares: {squares}\nCubes: {cubes}')