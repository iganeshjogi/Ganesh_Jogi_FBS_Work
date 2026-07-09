# 7. Python Program to Remove the Given Key from a Dictionary.

d = {
    'item1': 50,
    'item2': 120,
    'item3': 30,
    'item4': 200
}

def removekey(dictionary, key):
    if key in dictionary:
        dictionary.pop(key)
    else:
        return 'Key Not Found!'
    return dictionary


key = input('Enter key which to be remove: ')

res = removekey(d, key)

print(res)