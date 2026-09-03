from tkinter import *
from tkinter import messagebox

def Substraction():
    num1 = int(num1_entry.get())
    num2= int(num2_entry.get())
    minus = num1 - num2
    messagebox.showinfo(title='Output',message=f'The Substraction is {minus}.')

if (__name__ == '__main__'):
    window = Tk()

    window.title('SubStaction')
    window.geometry('500x500')
    window.config(background='Grey')

    txt1 = Label(window,text='Enter Big Number:')
    num1_entry = Entry(window)

    txt2 = Label(window,text='Enter Small Number:')
    num2_entry = Entry(window)

    txt1.pack()
    num1_entry.pack()

    txt2.pack()
    num2_entry.pack()

    button = Button(window, text='MINUS', command=Substraction) 
    button.pack()

    window.mainloop()