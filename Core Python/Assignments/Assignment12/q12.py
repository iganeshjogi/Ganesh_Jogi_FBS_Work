# 12. Python Program to count number of digits and letters in a string.

def countLettersDigits(string):
    digits = 0
    letters = 0
    for i in string:
        if i in '0123456789':
            digits += 1

        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            letters += 1
    
    return (f'Digits: {digits}\nLetters: {letters}')

string = input('Enter the String elements: ')

print(countLettersDigits(string))