#Cheking number is positive, negative or neutral

num = int(input('Enter number:'))
if(num == 0):
    print('The number is neutral.')
elif(num > 0):
    print('The number is positive.')
else:
    print('The number is nagative.')