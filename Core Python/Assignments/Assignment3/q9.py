#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = float(input('Enter the marks of subject 1: '))
sub2 = float(input('Enter the marks of subject 2: '))
sub3 = float(input('Enter the marks of subject 3: '))
sub4 = float(input('Enter the marks of subject 4: '))
sub5 = float(input('Enter the marks of subject 5: '))

percent = (sub1 + sub2 + sub3 + sub4 + sub5) / 500 * 100

if percent >= 75:
    print('First class.')
elif percent >= 50:
    print('Second class.')
elif percent >= 35:
    print('Third class.')
else:
    print('Fail')