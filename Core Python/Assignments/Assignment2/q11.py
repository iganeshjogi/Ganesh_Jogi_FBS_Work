#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input('Enter the amount:'))

note2000 = amount // 2000
amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10
print(f'2000 notes = {note2000}')
print(f'500 notes = {note500}')
print(f'200 notes = {note200}')
print(f'100 notes = {note100}')
print(f'50 notes = {note50}')
print(f'20 notes = {note20}')
print(f'10 notes = {note10}')

total_notes = note2000 + note500 + note200 + note100 + note50 + note20 + note10

print(f'Minimun notes required are {total_notes}.')