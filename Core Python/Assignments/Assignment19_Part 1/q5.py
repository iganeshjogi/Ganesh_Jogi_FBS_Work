# 5. Find all of the words in a string that are less than 5 letters (take input from user)

sentenace = input('Enter String: ')

n = [i for i in sentenace.split() if len(i) < 5]

print(f'words having less than 5 letters:\n{n}')