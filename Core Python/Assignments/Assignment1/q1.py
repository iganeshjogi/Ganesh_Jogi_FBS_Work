#Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input('Enter the marks of subject 1 out of 100:'))
sub2 = int(input('Enter the marks of subject 2 out of 100:'))
sub3 = int(input('Enter the marks of subject 3 out of 100:'))
sub4 = int(input('Enter the marks of subject 4 out of 100:'))
sub5 = int(input('Enter the marks of subject 5 out of 100:'))

total = (sub1 + sub2 + sub3 + sub4 + sub5)
percentage = total/500 * 100

print(f'The percentage of student is {percentage}%.')



