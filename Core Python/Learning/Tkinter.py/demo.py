from tkinter import *
    

if(__name__ == '__main__'):
    window = Tk()

    window.title('Demo')
    window.geometry('300x500')
    window.config(background='black')

    txt = Label(window, text= 'Hello World!')
    txt.pack()
    
    window.mainloop()