# 8. Python Program to Remove the Characters of Odd Index Values in a String

def RemoveOddIndex(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]
    return new_string


string = input('Enter the string elements: ')
print(RemoveOddIndex(string))