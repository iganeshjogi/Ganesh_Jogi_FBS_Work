'''
9. Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements. '''


def EvenOddListElementSep(li):
    even_li = []
    odd_li = []
    for i in li:
        if i % 2 == 0:
            even_li.append(i)
        else:
            odd_li.append(i)
    return (f'Even Elements List: {even_li}\nOdd Elements List: {odd_li}')

li = [42, 17, 88, 23, 56, 91, 34, 75, 60, 11]
print(EvenOddListElementSep(li))