from tkinter import *
from tkinter import ttk , messagebox
import sqlite3

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Book store app")
        self.minsize(600,300)
        self.configure(background='#b97a57')
        self.iconbitmap('E:/barname_nevisi/python/pybootcamp/03/project3/list_format/icon.ico')
        self.items=[]
        self.create_ui()
        
    def create_ui(self):
        labelframe1=LabelFrame(self,text='Register Book',bg='#b97a57')
        labelframe1.grid(row=0 , column= 0,padx=5, pady=5, ipadx=0, ipady=0)
        self.booktitle = StringVar()
        self.label1 = Label(labelframe1, text='Title :',bg='#b97a57')
        self.label1.grid(row = 0 , column = 0, padx=0, pady=5, ipadx=0, ipady=0)
        self.Entry1 = Entry(labelframe1,bg='#efe4b0', textvariable = self.booktitle)
        self.Entry1.grid(row = 0 , column = 1, padx=0, pady=5, ipadx=0, ipady=0)
        
        self.bookauthor = StringVar()
        self.label2 = Label(labelframe1, text='Author :',bg='#b97a57')
        self.label2.grid(row = 1 , column = 0, padx=0, pady=5, ipadx=0, ipady=0)
        self.Entry2 = Entry(labelframe1, bg='#efe4b0',textvariable = self.bookauthor)
        self.Entry2.grid(row = 1 , column = 1, padx=0, pady=5, ipadx=0, ipady=0)
        
        self.bookyear = StringVar()
        self.label3 = Label(labelframe1, text='Year :',bg='#b97a57')
        self.label3.grid(row = 2 , column = 0, padx=0, pady=5, ipadx=0, ipady=0)
        self.Entry3 = Entry(labelframe1,bg='#efe4b0', textvariable = self.bookyear)
        self.Entry3.grid(row = 2 , column = 1, padx=0, pady=5, ipadx=0, ipady=0)
        
        self.bookisbn = StringVar()
        self.label4 = Label(labelframe1, text='ISBN :',bg='#b97a57')
        self.label4.grid(row = 3 , column = 0, padx=0, pady=5, ipadx=0, ipady=0)
        self.Entry4 = Entry(labelframe1,bg='#efe4b0', textvariable = self.bookisbn)
        self.Entry4.grid(row = 3 , column = 1, padx=0, pady=5, ipadx=0, ipady=0)
        

        self.button1 = ttk.Button(labelframe1 , text='Submit',command=self.Submit)
        self.button1.grid(row = 4 , column = 0,padx=5, pady=5)
        
        self.button2 = ttk.Button(labelframe1 , text='Delete',command=self.Delete)
        self.button2.grid(row = 4 , column = 1,padx=5, pady=5)

        self.button3 = ttk.Button(labelframe1 , text='Update',command=self.Update)
        self.button3.grid(row = 4 , column = 2,padx=5, pady=5)
        
        
        labelframe2=LabelFrame(self,text='Books',bg='#b97a57')
        labelframe2.grid(row=0 , column= 1 , rowspan = 2,padx=5,pady=5)

        self.listbox =Listbox(labelframe2,height=18,width=100,bg='#efe4b0')
        self.Showall()
        self.listbox.bind('<<ListboxSelect>>',self.Selectitem)
        self.scroll = Scrollbar(labelframe2,command=self.listbox.yview)
        self.listbox.configure(yscrollcommand = self.scroll.set)
        self.listbox.pack(side=LEFT)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.scroll.pack(side=RIGHT,fill=Y)
        
        labelframe3=LabelFrame(self,text='Search',bg='#b97a57')
        labelframe3.grid(row=1,column=0, padx=5, pady=5, ipadx=0, ipady=0)
        

        self.titlesearch = StringVar()
        self.authorsearch = StringVar()
        self.label5 = Label(labelframe3, text='Search Title :',bg='#b97a57')
        self.label5.grid(row = 0 , column = 0 , padx=5, pady=5, ipadx=0, ipady=0)
        self.label6 = Label(labelframe3, text='Search Author :',bg='#b97a57')
        self.label6.grid(row = 1 , column = 0, padx=5, pady=5, ipadx=0, ipady=0)
        self.searchtitle = Entry(labelframe3,bg='#efe4b0', textvariable = self.titlesearch)
        self.searchtitle.grid(row = 0 , column = 1, padx=5, pady=5, ipadx=0, ipady=0)
        self.searchauthor = Entry(labelframe3,bg='#efe4b0', textvariable = self.authorsearch)
        self.searchauthor.grid(row = 1 , column = 1, padx=5, pady=5, ipadx=0, ipady=0)
        self.button4 = ttk.Button(labelframe3 , text='Search',command=self.Search1)
        self.button4.grid(row = 0 , column = 2,padx=5, pady=5)
        self.button5 = ttk.Button(labelframe3 , text='Search',command=self.Search2)
        self.button5.grid(row = 1 , column = 2,padx=5, pady=5)
        self.button6 = ttk.Button(labelframe3 , text='Showall',command=self.Showall)
        self.button6.grid(row = 2 , column = 1,padx=5, pady=5)
    def DeleteEntrys(self):
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
    def Showall(self):
        with sqlite3.connect("database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books")
                self.listbox.delete(0,'end')
                for row in cursor:
                    self.listbox.insert('end',row) 
        
    def Selectitem(self,event):
        self.items = self.listbox.get(ANCHOR)
        
        self.Entry1.delete(0,END)
        self.Entry2.delete(0,END)
        self.Entry3.delete(0,END)
        self.Entry4.delete(0,END)
        
        self.Entry1.insert(0,self.items[1])
        self.Entry2.insert(0,self.items[2])
        self.Entry3.insert(0,self.items[3])
        self.Entry4.insert(0,self.items[4])
    def Update(self):
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute( "UPDATE books SET Title=? , Author=? , Year=? , ISBN=? WHERE id=?",(self.booktitle.get(),self.bookauthor.get(),self.bookyear.get(),self.bookisbn.get(),self.items[0],) )
            conn.commit()
            self.DeleteEntrys()
            self.Showall()
        messagebox.showinfo(title='Updated',message='The Your Book Updated.')

    def Search1(self):
        self.listbox.delete(0,END)
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute( "SELECT * from books WHERE Title = ?",(self.titlesearch.get(),) )
            for row in cursor:
                self.listbox.insert('end',row)

    def Search2(self):
        self.listbox.delete(0,END)
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute( "SELECT * from books WHERE Author = ?",(self.authorsearch.get(),) )
            for row in cursor:
                self.listbox.insert('end',row)       
    def Submit(self):
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute( "INSERT INTO books VALUES (NULL,?,?,?,?)"  ,  (self.booktitle.get(),self.bookauthor.get(),self.bookyear.get(),self.bookisbn.get())  )
            conn.commit()
        
        messagebox.showinfo(title='Submitted',message='The Book {} Submitted.'.format(self.booktitle.get()))
        self.DeleteEntrys()
        self.Showall()
        
    def Delete(self):
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute( "DELETE FROM books WHERE id=?",(self.items[0],) )
            conn.commit()
            self.DeleteEntrys()
            self.Showall()
        messagebox.showinfo(title='Deleted',message='The Book {} Deleted.'.format(self.booktitle.get()))

           
        
root = Root()
root.mainloop()
