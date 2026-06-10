# 6. Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fibonacciSeries(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        print (b, end=' ')
        c = a + b
        a = b
        b = c
    
n = int(input('Enter the last number: '))
fibonacciSeries(n)