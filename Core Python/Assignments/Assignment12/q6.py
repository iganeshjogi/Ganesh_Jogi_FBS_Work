# 6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

def space_replace(string):
    new_string = ''
    for i in string:
        if i != ' ':
            new_string += i
        else:
            new_string += '-'
    return new_string

string = input('Enter the String Elements: ')
print(space_replace(string))