# 2. Python Program to Concatenate Two Dictionaries Into One

dict1 = {'Name' : 'Ganesh'}
dict2 = {'Roll No' : 101}


def concatDictionary(dict1, dict2):
    for i in dict2:
        dict1[i] = dict2[i]


concatDictionary(dict1, dict2)

print(dict1)