from tkinter import *
from tkinter import messagebox

def apply():
    val = var.get()
    if (val == 1):
        window.config(background= 'Black')
    elif (val == 2):
        window.config(background= 'Blue')
    elif (val == 3):
        window.config(background= 'Red')
    else:
        messagebox.showwarning(title='Error',message='Color is not selected.')

if(__name__ == '__main__'):
    window = Tk()
    window.geometry('300x400')

    var = IntVar()
    
    txt = Label(window, text= 'Please select color:')
    rdo1 = Radiobutton(window, text='Black', variable=var, value=1)
    rdo2 = Radiobutton(window, text='Blue', variable=var, value=2)
    rdo3 = Radiobutton(window, text='Red', variable=var, value=3)

    btn = Button(window, text='Apply', command=apply)

    txt.pack()
    rdo1.pack()
    rdo2.pack()
    rdo3.pack()
    btn.pack()

    window.mainloop()