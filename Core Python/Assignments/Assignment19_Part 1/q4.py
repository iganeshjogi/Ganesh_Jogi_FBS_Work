# 4. Remove all of the vowels in a string (take input from user).

sentenace = input('Enter String: ')

n = [i for i in sentenace if i not in 'aeiouAEIOU']

x = ''.join(n)

print(f'String without vowels:\n{x}')