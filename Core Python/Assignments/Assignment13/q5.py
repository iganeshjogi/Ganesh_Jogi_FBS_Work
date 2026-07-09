# 5. Python Program to Sum All the Items in a Dictionary.

d = {
    'item1': 50,
    'item2': 120,
    'item3': 30,
    'item4': 200
}

def dictionaryItemsSum(dictionary):

    count = 0
    for i in dictionary:
        value = dictionary[i]
        count += value
    return count

total = dictionaryItemsSum(d)

print(f'The Sum of all the items in the dictionary is {total}.')