### keyword variable length argument
#1. To pass multiple value to function with meaning
#2. Mention two asterisk ** symbols before para name in function defination
#3. keywords and values are stored in dictionary format
#4. use for loop on dict.items() to iterate data individually

def emp(**data):
    for key,val in data.items():
        print(key,':',val)


emp(name='Ganesh',id=101,salary=50000)