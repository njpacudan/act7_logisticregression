import tkinter as tk
from tkinter import *
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="cnpetstore"
)
c = db.cursor()
class Mainpage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x300")
        self.title('Completely Normal Pet Shop')

        topframe = tk.Frame(self, bg = 'orange', bd=10)
        storename ='Completely Normal Pet Shop'
        messageVar = Message(topframe, text = storename, width=700, bg='orange')
        messageVar.config(font=('MS Serif',37))
        messageVar.pack(anchor = NW)

        avaframe = tk.Frame(self, bg='white',bd=10)
        ava = Label(avaframe, text="Available Pets for Sale!", bg='white')
        ava.config(font=('Ms Serif', 15))
        ava.pack(anchor = NW)

        menu = Menu()
        self.config(menu=menu)
        options = Menu(menu)
        menu.add_cascade(label='Options', menu=options)
        options.add_command(label='Add New Pet')
        options.add_command(label='Modify Pet Stock', command= ModifyStock)
        options.add_command(label='Delete Pet')
        options.add_separator()
        options.add_command(label='Exit', command=self.quit)


        middleframe = tk.Frame(self, bg='white')
        l1 = Label(middleframe, text="Pet ID", font=('Ms Serif', 12,), fg='blue', bg='white')
        l1.grid(column=0,row=0)
        l2 = Label(middleframe, text="Name", font=('Ms Serif', 12,), fg='blue', bg='white')
        l2.grid(column=1,row=0)
        l3 = Label(middleframe, text="Price", font=('Ms Serif', 12,), fg='blue', bg='white')
        l3.grid(column=2,row=0)
        l4 = Label(middleframe, text="Stock", font=('Ms Serif', 12,), fg='blue', bg='white')
        l4.grid(column=3,row=0)
        c.execute("SELECT * FROM pets")
        i=1
        for pets in c:
            for j in range(len(pets)):
                e = Entry(middleframe, width=10, fg='blue')
                e.config(font=('Ms Serif', 10))
                e.grid(row=i, column=j)
                e.config(state=NORMAL)
                e.insert(END, pets[j])
                e.config(state=DISABLED)
            i=i+1
        topframe.pack(side = TOP, fill=X)
        avaframe.pack(anchor=NW, fill=X)
        middleframe.pack(anchor=NW)
        
class ModifyStock (Toplevel):
    def __init__(self):
        super().__init__()
        def check1():
            if d == ans1:
                l2 = Label(storelabels, text="Input New Pet Stock",font=('Ms Serif', 10,), bg='white')
                l2.grid(column=0, row=1)
                e2 = Entry(storelabels)
                e2.grid(column=1, row=1)
                ans2 = e2.get()
            else:
                l2 = Label(storelabels, text="Pet ID not Detected!",font=('Ms Serif', 10,), bg='white')
                l2.grid(column=0, row=1)
        self.geometry("300x80")
        self.title('Completely Normal Pet Shop || Modify Pet Stock')
        storelabels = tk.Frame(self, bg='white')
        l1 = Label(storelabels, text="Input Pet ID",font=('Ms Serif', 10,), bg='white')
        l1.grid(column=0, row=0)
        e1 = Entry(storelabels)
        e1.grid(column=1, row=0)
        ans1 = e1.get()
        check_stock = "SELECT petstock FROM pets WHERE petid = %s"
        tuple1 = (ans1,)
        c.execute(check_stock,tuple1)
        stock_result = c.fetchone()
        d = stock_result[0]
        b1 = Button(storelabels, text='Check', command=check1)
        b1.grid(column=2, row=0)
        storelabels.pack(anchor=W)
if __name__ == "__main__":
    app = Mainpage()
    app.mainloop()