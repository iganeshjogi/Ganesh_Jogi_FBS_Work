# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace_character(string,a,b):
    new_str = ''
    for i in string:
        if i != a:
            new_str = new_str + i
        else:
            new_str = new_str + b
    return new_str

string = input('Enter the string elements: ')
a = input('What to replace: ')
b = input('By what to replace: ')

print(replace_character(string, a, b))