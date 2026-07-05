# 11. Python Program to count number of lowercase characters in a string.

def countLowercase(string):
    count = 0
    for i in range(len(string)):
        if string[i] in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
    return (f'Count of Lowercase characters: {count}')


string = input('Enter the String elements: ')
print(countLowercase(string))