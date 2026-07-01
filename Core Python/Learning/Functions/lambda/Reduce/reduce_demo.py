# Method 1 for importing
'''
import functools

data = [1,2,3,4,5,6,7,8,9,10]

res = functools.reduce(lambda x,y:x+y,data)
print(res) 
'''

# Method 2 for importing

from functools import reduce

data = [1,2,3,4,5,6,7,8,9,10]

print(reduce(lambda x,y: x+y,data))