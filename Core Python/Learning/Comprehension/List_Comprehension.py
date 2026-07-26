## print 1 to n.

# li = [ val for val in range(1,11)] 
# print(li)


## Print even numbers

# li = [ val for val in range(1,11) if val % 2 == 0] 
# print(li)


## Print  Lists in list

# li1 = [[j for j in range (i * 10 + 1, (i +1) * 10 + 1)] for i in range (0, 10)]
# print(li1)


## print squares

# sqr = [i*i for i in range(1, 21)]
# print(sqr)


## find the aleternate numbers between any range

s = int(input('Enter the start Number: '))
n = int(input("Enter the last Number: "))
alt = [num for num in range(s, n+1, 2)]
print(alt)