'''Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill'''

units = int(input('Enter the electricity units: '))

if units <= 50:
    charges = units * 0.50

elif units > 50 and units <= 150:
    charges = (50 * 0.50) + ((units - 50) * 0.75)

elif units > 150 and units <= 250:
    charges = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

else:
    charges = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + (( units - 250) * 1.50)

surcharge = (20/100) * charges

total_bill = charges + surcharge

print(f'Electricity bill is {total_bill} rs.')