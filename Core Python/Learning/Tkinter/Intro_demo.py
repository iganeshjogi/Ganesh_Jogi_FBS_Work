from tkinter import *

if __name__ == '__main__':
    window = Tk()

    window.title('My Intro')
    window.geometry('500x500')
    window.config(background='Grey')

    txt1 = Label(window,text='My name is Ganesh')
    txt1.pack()
    txt2 = Label(window,text='I am from Latur')
    txt2.pack()

    window.mainloop()