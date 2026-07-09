# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not.

dictionary = {'Name' : 'Ganesh', 'City' : 'pune' }

def keyOccurancechk(dictionary, keys):
    if keys in dictionary:
        return True
    else:
        return False
    
keys = 'Name'
res = keyOccurancechk(dictionary, keys)

print(res)