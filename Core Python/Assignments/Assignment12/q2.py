# 2. Python Program to Remove the nth Index Character from a Non-Empty String

def remove_nth_index(string,n):
    new_string = ''
    for i in range(0,len(string)):
        if i != n:
            new_string += string[i]
    return new_string

string = input('Enter the String Elements: ')
n = int(input('Enter the nth Index to remove element: '))

print(remove_nth_index(string,n))