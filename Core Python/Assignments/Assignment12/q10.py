# 10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.

def large_String (string1, string2):
    count1 = 0
    count2 = 0

    for i in string1:
        count1 += 1

    for j in string2:
        count2 += 1
    
    if count1 > count2:
        return 'string1'
    elif count1 == count2:
        return 'Both Equal'
    else:
        return 'string2'
    

string1 = input('Enter the String1 Elements: ')
string2 = input('Enter the String2 Elements: ')   

res = large_String(string1,string2)
print(f'Largest string: {res}')

