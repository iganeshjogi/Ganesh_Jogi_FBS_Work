# 3. Count the number of spaces in a string (take input from user).

sentenace = input('Enter String: ')

spaces = len([i for i in sentenace if i == ' '])

print(f'Count of spaces: {spaces}')