# 1. Python Program to Add a Key-Value Pair to the Dictionary

student = {'Name': 'Ganesh', 'RollNo': 101 }

def AddKeyValuePair(dictinary, key, value):
    dictinary[key] = value

key = input('Enter the key: ')
value = input('Enter the Value: ')

AddKeyValuePair(student, key, value )

print(student)