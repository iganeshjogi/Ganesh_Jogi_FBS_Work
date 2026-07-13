# 8. Write a Python program to find all the anagrams and group them together from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = {}

for word in words:

    key = ''.join(sorted(word))
    
    if key not in anagrams:
        anagrams[key] = []

    anagrams[key].append(word)

print(anagrams)

for group in anagrams.values():
    print(group)