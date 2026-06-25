#Marrige eligibility check

gender = input('Enter the gender (male / female):')
age = int(input('Enter age:'))

if gender == 'male':
    if age >= 21:
        print('Eligible')
    else:
        print('Not Eligible')
else:
    if gender == 'female':
        if age >= 18:
            print('Eligible')
        else:
            print('Not Eligible')