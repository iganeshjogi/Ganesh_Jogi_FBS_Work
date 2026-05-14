#Write a program to convert days into years, weeks and days.

days = int(input('enter the days:'))

years = days // 365
days = days % 365
weeks = days // 7
days = days % 7

print(f"years: {years}, weeks: {weeks}, days: {days}")