#Write a program to calculate profit or loss.

cp = float(input('Enter the cost price: '))
sp = float(input('Enter the selling price: '))

if sp > cp:
    print('profit')

elif sp == cp:
    print('Equal')
else:
    print('Loss')