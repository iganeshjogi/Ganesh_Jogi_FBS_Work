# 1. Write a Python program to find elements in a given set that are not in another set.

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

# Method 1:

def SetDifferencelements(s1,s2):
    for i in s1:
        if i not in s2:
            print(i)
        
SetDifferencelements(s1,s2)

# Method 2:

# print(s1 - s2)