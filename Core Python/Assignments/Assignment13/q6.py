# 6. Python Program to Multiply All the Items in a Dictionary.

d = {
    'item1': 5,
    'item2': 12,
    'item3': 3,
    'item4': 2
}

def multiplyDictionaryItems(dictionary):
    
    multiplication = 1
    for i in dictionary:
        value = dictionary[i]
        multiplication *= value
    return multiplication

total_multiplication = multiplyDictionaryItems(d)

print(f'The Multiplication of all items in a dictionary is {total_multiplication}.')