from tkinter import *
from tkinter import messagebox

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()

def empManage():
    clearScreen()
    def loadData():
        with open('Core Python/Demos/Tkinter.py/empdatatxt', 'r') as fp:
            for line in fp:
                mylist.insert(END, line.strip('\n'))

    def addEmp():
        id = id_entry.get()
        nm = nm_entry.get()
        sal = sal_entry.get()

        emp_data = f'{id}, {nm}, {sal}'
        with open('Core Python/Demos/Tkinter.py/empdatatxt', 'a') as fp:
            fp.write(emp_data+'\n')

        mylist.insert(END, emp_data)
        messagebox.showinfo(title='NOTICE', message='Employee Added Successfully.')

    def selEmp():
        data = mylist.get(ACTIVE)
        emp_list = data.split(', ')
        id_entry.insert(0, emp_list[0])
        nm_entry.insert(1, emp_list[1])
        sal_entry.insert(2, emp_list[2])

    def updEmp():
        pass

    def delEmp():
        pass

    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)

    id_txt = Label(frame1, text='ID')
    nm_txt = Label(frame1, text='Name')
    sal_txt = Label(frame1, text='SALARY')

    id_entry = Entry(frame1)
    nm_entry = Entry(frame1)
    sal_entry =Entry(frame1)

    id_txt.grid(row=0, column=0)
    id_entry.grid(row=0, column=1)
    nm_txt.grid(row=1, column=0)
    nm_entry.grid(row=1, column=1)
    sal_txt.grid(row=2, column=0)
    sal_entry.grid(row=2, column=1)

    frame1.pack()

    add_btn = Button(frame2, text='ADD', command=addEmp)
    sel_btn = Button(frame2, text='SELECT', command=selEmp)
    upd_btn = Button(frame2, text='UPDATE', command=updEmp)
    del_btn = Button(frame2, text='DELETE', command=delEmp)

    add_btn.pack(side=LEFT)
    sel_btn.pack(side=LEFT)
    upd_btn.pack(side=LEFT)
    del_btn.pack(side=LEFT)
    frame2.pack()

    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(frame3, yscrollcommand=scrollbar.set, height=15, width=30)
    mylist.pack(side=LEFT, fill=BOTH)

    scrollbar.config(command=mylist.yview)

    frame3.pack()

    loadData()
def login():
    uid = uid_entry.get()
    passw = passw_entry.get()
    if(uid == 'admin' and passw == '12345'):
        empManage()
    else:
        messagebox.showerror('ERROR', message='Invalid Credentials')

def main():

    uid_txt = Label(window, text='Enter UID:')
    global uid_entry
    uid_entry = Entry(window)

    passw_txt = Label(window, text='Enter PASSWORD:')
    global passw_entry
    passw_entry = Entry(window)

    login_btn = Button(window, text='LOGIN', command=login)

    uid_txt.pack()
    uid_entry.pack()
    passw_txt.pack()
    passw_entry.pack()
    login_btn.pack()

if(__name__ == '__main__'):

    window = Tk()
    window.geometry('300x400')
    window.title('Employee Management System')
    main()
    

    window.mainloop()