# 7. Python Program to Calculate the Length of a String Without Using a Library Function

def length_calculator(string):
    count = 0
    for i in string:
        count += 1
    return count

string = input('Enter the string Elements: ')
print(length_calculator(string))