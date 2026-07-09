# 8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.


s = input('Enter the string: ')

def stringWordsFrequencyCount(s):
    
    # s = s.lower()
    snew = s.split()

    frequency = {}

    for i in snew:

        if i in frequency:
            frequency[i] += 1

        else:
            frequency[i] = 1
        
    return frequency

res = stringWordsFrequencyCount(s)

print(res)