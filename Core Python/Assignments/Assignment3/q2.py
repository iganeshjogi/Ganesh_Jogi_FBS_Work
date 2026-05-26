# Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = str(input('Enter the alphabet: '))

if alphabet in 'AEIOUaeiou':
    print(f'The {alphabet} is vowel.')
else:
    print(f'The {alphabet} is consonant.')