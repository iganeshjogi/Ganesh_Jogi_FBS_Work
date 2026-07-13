''' 6. Write a Python program to find the two numbers whose product is 
maximum among all the pairs in a given list of numbers. Use the
Python set.'''

num = [2, 5, 6, 3, 9, 0]

product = 0
first = num[0]
second = num [1]
max_product = 0

for i in range(len(num)):
    for j in range(i+1,len(num)):
        product = num[i] * num[j]
        if product > max_product:
            first = num[i]
            second = num[j]
            max_product = product

print(f'Numbers: ({first}, {second})') 
print(f'Maximum product: {max_product}')