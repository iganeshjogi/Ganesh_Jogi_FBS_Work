# 12. Write a program to create three lists of numbers, their squares and cubes

li = [1, 2, 3, 4, 5]

def listsquaresandcubes(li):
    square_li = []
    cube_li = []
    for i in li:
        square_li.append(i**2)
        cube_li.append(i**3)
    return (f'Numbers: {li}\nSquares: {square_li}\nCubes: {cube_li}')

print(listsquaresandcubes(li))