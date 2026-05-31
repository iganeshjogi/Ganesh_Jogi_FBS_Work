'''2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.'''
av_percentage = 0
n = int(input('Enter number of students:'))
for i in range(1,n+1):
    sub1 = float(input('Enter the marks of subject 1: '))
    sub2 = float(input('Enter the marks of subject 2: '))
    sub3 = float(input('Enter the marks of subject 3: '))
    sub4 = float(input('Enter the marks of subject 4: '))
    sub5 = float(input('Enter the marks of subject 5: '))

    percentage = (sub1 + sub2 + sub3 + sub4 + sub5)/500 * 100
    print(f'percentage of student is {percentage}%')

    av_percentage += percentage

av_percentage = av_percentage / n
print(f'Average percentage of students is {av_percentage}%')
