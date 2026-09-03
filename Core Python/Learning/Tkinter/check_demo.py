from tkinter import *
from tkinter import messagebox

def buy():
    val1 = x.get()
    val2 = y.get()
    val3 = z.get()
    products = ''
    if (val1 == 1):
        products += 'Shirt/Top\n'
    if (val2 == 1):
        products += 'Jeans\n'
    if (val3 == 1):
        products += 'Shoes'

    if(products):
        messagebox.showinfo(message=f'You bought:\n{products}')
    else:
        messagebox.showwarning(message='Nothing selected!')

if(__name__ == '__main__'):
    window = Tk()
    window.geometry('300x400')
    window.title('Shopping')
    x = IntVar()
    y = IntVar()
    z = IntVar()
    txt = Label(window, text='Select option from below:')

    chk1 = Checkbutton(window, text= 'Shirts/Top', variable=x)
    chk2 = Checkbutton(window, text= 'Jeans', variable=y)
    chk3 = Checkbutton(window, text= 'Shoes', variable=z)
    btn = Button(window, text='BUY', command= buy)

    txt.pack()
    chk1.pack()
    chk2.pack()
    chk3.pack()
    btn.pack()
    window.mainloop()