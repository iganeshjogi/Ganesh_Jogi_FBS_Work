from tkinter import *
from tkinter import messagebox

def addition():
    num1 = int(num1_entry.get())
    num2 = int(num2_entry.get())
    sum = num1 + num2
    messagebox.showinfo(title='Output', message=f'Addition is {sum}.')

if(__name__ == '__main__'):
    window = Tk()
    window.title('Addition')
    window.geometry('300x400')
    window.config(background='grey')

    txt1 = Label(window, text='Enter number 1:')
    num1_entry = Entry(window)

    txt2 = Label(window, text='Enter number 2:')
    num2_entry = Entry(window)

    txt1.pack()
    num1_entry.pack()

    txt2.pack()
    num2_entry.pack()

    button = Button(window, text='ADD', command=addition)
    button.pack()

    window.mainloop()

    