try:

    li = [10, 20, 30]
    print(li.index(int(input('Enter the Number: '))))
    print(li[50])

# Specialied expection handling
except ValueError as e:
    print('Value error:', e)

except IndexError as e:
    print('Index error', e)

# Generalized expetion handling
except Exception as e:
    print('Error', e)

print('Program successfully completed.')