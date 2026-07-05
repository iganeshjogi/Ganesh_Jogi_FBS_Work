# 3. Python Program to Detect if Two Strings are Anagrams

def anagram_check(string1, string2):

    if len(string1) != len(string2):
        return 'Not Anagram'
    
    for i in string1:

        count1 = 0
        count2 = 0
        
        for j in string1:
            if i == j :
                count1 += 1

        for k in string2:
            if k == i:
                count2 += 1
        
        if count1 != count2:
            return 'Not Anagram'

    
    return 'Anagram'

string1 = input('Enter the String 1 elements: ')
string2 = input('Enter the String 2 elements: ')

print(anagram_check(string1, string2))