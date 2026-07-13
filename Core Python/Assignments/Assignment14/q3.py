# 3. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. 
#    Use Python set data type.

string = input('Enter the string: ')

li = string.split()

frequency = {}

for word in li:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

print("Unique Words :", set(li))