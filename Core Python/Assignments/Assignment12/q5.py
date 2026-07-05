# 5. Python Program to Count the Number of Vowels in a String5. Python Program to Count the Number of Vowels in a String.

def vowels_count(string):
    count = 0
    for i in range(len(string)):
        if string[i] in 'aeiouAEIOU':
            count += 1
    return count


string = input('Enter String Elemnts: ')
print(vowels_count(string))