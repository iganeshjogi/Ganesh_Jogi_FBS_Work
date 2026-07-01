### variable length parameter/argument
#1. To pass multiple values in Function
#2. Mention asterisk * symbol before parameter name in function defination
#3. Passed values will be stored as a tuple
#4. Use for loop to get Individual value

def add(*num):
    sum = 0
    for val in num:
        sum += val
    return sum

res = add(1,2,3,4,5,6,7,8,9,10)
print(res)