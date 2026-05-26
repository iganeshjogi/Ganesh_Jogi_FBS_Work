'''Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

price = 1000
person1 = int(input('Enter the age of person1:'))
person2 = int(input('Enter the age of person2:'))
person3 = int(input('Enter the age of person3:'))
person4 = int(input('Enter the age of person4:'))
person5 = int(input('Enter the age of person5:'))

#person1

if person1 < 12:
    ticket1 = price - (30 / 100) * price
    print(f'Ticket for person 1 is {ticket1} rs.')

elif person1 > 59:
    ticket1 = price - (50 / 100) * price
    print(f'Ticket for person 1 is {ticket1} rs.')

else:
    ticket1 = price
    print(f'Ticket for person 1 is {price} rs.')

#person2

if person2 < 12:
    ticket2 = price - (30 / 100) * price
    print(f'Ticket for person 2 is {ticket2} rs.')

elif person2 > 59:
    ticket2 = price - (50 / 100) * price
    print(f'Ticket for person 2 is {ticket2} rs.')

else:
    ticket2 = price
    print(f'Ticket for person 2 is {price} rs.')

#person3

if person3 < 12:
    ticket3 = price - (30 / 100) * price
    print(f'Ticket for person 3 is {ticket3} rs.')

elif person3 > 59:
    ticket3 = price - (50 / 100) * price
    print(f'Ticket for person 3 is {ticket3} rs.')

else:
    ticket3 = price
    print(f'Ticket for person 3 is {price} rs.')

#person4

if person4 < 12:
    ticket4 = price - (30 / 100) * price
    print(f'Ticket for person 4 is {ticket4} rs.')

elif person4 > 59:
    ticket4 = price - (50 / 100) * price
    print(f'Ticket for person 4 is {ticket4} rs.')

else:
    ticket4 = price
    print(f'Ticket for person 4 is {price} rs.')

#person5

if person5 < 12:
    ticket5 = price - (30 / 100) * price
    print(f'Ticket for person 5 is {ticket5} rs.')

elif person5 > 59:
    ticket5 = price - (50 / 100) * price
    print(f'Ticket for person 5 is {ticket5} rs.')

else:
    ticket5 = price
    print(f'Ticket for person 5 is {price} rs.')

total_ticket =  ticket1 + ticket2 + ticket3 + ticket4 + ticket5

print(f'Total ticket amount is {total_ticket} rs.')