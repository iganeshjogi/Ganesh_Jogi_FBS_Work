'''
1. Develop a simple calculator program that performs basic arithmetic operations 
(+, -, *, /) on two numbers provided by the user. The program should ask the user for
the numbers and the operator. 
However, the program should handle the following exceptions:

    a. Invalid Number: If the user enters a number that is not valid, catch the
    exception and display an error message.
    b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
    "/", catch the exception and display an error message.
    c. Division by Zero: If the user tries to divide by zero, catch the exception and
    display an error message.

Write a program that performs the requested arithmetic operation and
handles the exceptions as described above.'''

try:
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))

    op = input('Enter Operator: ')

    if op == '+':
        print("Result =", num1 + num2)

    elif op == '-':
        print("Result =", num1 - num2)

    elif op == '*':
        print("Result =", num1 * num2)

    elif op == '/':
        print("Result =", num1 / num2)

    else:
        raise Exception('Invalid Operator.')


except ValueError:
    print('Error: Please enter valid numbers.')

except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')

except Exception as e:
    print('Error:', e)
