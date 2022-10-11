import backend
from tkinter import *

def command_view():
    list1.delete(0, END)
    for res in backend.view():
        list1.insert(END, res)
def command_search():
    list1.delete(0, END)
    for res in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, res)
def add_command():
    list1.delete(0, END)
    backend.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    command_view()
    clear_text()
def clear_text():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
def command_update():
    indices = list1.curselection()
    row = list1.get(indices)
    ID = row[0]
    if len(title_text.get())!= 0:
        backend.update(ID,title_text.get(), row[2], row[3], row[4])
    if len(author_text.get())!= 0:
        backend.update(ID,row[1], author_text.get(), row[3], row[4])
    if len(year_text.get())!= 0:
        backend.update(ID,row[1], row[2], year_text.get(), row[4])
    if len(ISBN_text.get())!= 0:
        backend.update(ID,row[1], row[2], row[3], ISBN_text.get())
    command_view()
    clear_text()

def command_delete():
    rindex = list1.curselection()
    row = list1.get(rindex)
    ID = row[0]
    backend.delete(ID)
    command_view()

window = Tk()
window.title("BookDB")

l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
en1 = Entry(window, textvariable=title_text)
en1.grid(row=0,column=1)

author_text = StringVar()
en2 = Entry(window, textvariable=author_text)
en2.grid(row=1,column=1)

year_text = StringVar()
en3 = Entry(window, textvariable=year_text)
en3.grid(row=0,column=3)

ISBN_text = StringVar()
en4 = Entry(window, textvariable=ISBN_text)
en4.grid(row=1,column=3)

b1 = Button(window, text="View All",height=1,width=10, command=command_view)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry",height=1,width=10, command=command_search)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry",height=1,width=10, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update",height=1,width=10, command=command_update)
b4.grid(row=5, column=3)

b4 = Button(window, text="Delete",height=1,width=10, command=command_delete)
b4.grid(row=6, column=3)

b4 = Button(window, text="Close",height=1,width=10, command=window.destroy)
b4.grid(row=7, column=3)

list1=Listbox(window, width=35, height=10)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1= Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
window.mainloop()