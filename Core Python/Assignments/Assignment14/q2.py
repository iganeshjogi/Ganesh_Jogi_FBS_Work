# 2. Write a Python program to remove the intersection of a second set with a first set.

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

for i in s1.copy():
    if i in s2:
        s1.remove(i)
print(s1)