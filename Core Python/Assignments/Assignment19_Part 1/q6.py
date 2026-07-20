# 6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

sentenace = input('Enter String: ')
words = sentenace.split()
d = {word: len(word) for word in words }

print(d)