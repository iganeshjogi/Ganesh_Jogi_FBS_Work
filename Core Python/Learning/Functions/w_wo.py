#with passing parameter (with input)
#without returning value (without output) 
def add(num1,num2):

    sum = num1 + num2 
    print(f'Sum of {num1} and {num2} is {sum}')

x = int(input('Enter the number1: '))
y = int(input('Enter the number2: '))

add(x,y)