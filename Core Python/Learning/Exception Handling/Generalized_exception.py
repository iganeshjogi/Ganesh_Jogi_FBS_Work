
try:
    
    num1 = int(input('Enter the number 1: '))
    num2 = int(input('Enter the number 2: '))

# Generalized expection handling
except Exception as e:
    print('Error:', e)

else:
    sum = num1 + num2
    print('Addition is', sum)