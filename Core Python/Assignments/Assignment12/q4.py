# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged.

string = ''
def swap_first_last(string):
    new_string = ''
    for i in range(0,len(string)):
        if i == 0:
            new_string += string[-1]

        if i != 0 and i != len(string)-1 :
            new_string += string[i]

        if i == len(string)-1:
            new_string += string[0]
    return new_string

string = input('Enter string elements: ')
print(swap_first_last(string))