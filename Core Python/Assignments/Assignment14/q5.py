# 5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]

prefix = ""

first = words[0]

for i in range(len(first)):

    for word in words[1:]:

        if i >= len(word) or word[i] != first[i]:
            print(prefix)
            exit()

    prefix += first[i]

print(prefix)