''' 7. Given two sets of numbers, write a Python program to find the missing
numbers in the second set as compared to the first and vice versa.
Use the Python set. '''

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 4, 6, 9, 12}

def SetDifference(s1, s2):
    set1 = set()
    set2 = set()
    for i in s1:
        if i not in s2:
            set1.add(i)
    for j in s2:
        if j not in s1:
            set2.add(j)
    return set1, set2


missing_in_s2, missing_in_s1 = SetDifference(s1, s2)

print("Missing in set 2:", missing_in_s2)
print("Missing in set 1:", missing_in_s1)        