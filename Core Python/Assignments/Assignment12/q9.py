# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.

def words_Characters_Counter(string):
    characters = 0
    words = 0
    spaces = 0
    for i in string:
        characters += 1
        if i == ' ':
            spaces += 1
        words = spaces + 1
    return (f'characters: {characters}\nWords: {words}')


string = input('Enter the String elements: ')

print(words_Characters_Counter(string))