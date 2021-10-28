from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import psycopg2

from MyMessageBox import MyMessageBox
from book_manager import Book


def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, returnView, Canvas1, status

    bcode = bookInfo1.get()
    member_id = bookInfo2.get()
    retbook = Book(bcode, member_id=member_id)
    result = retbook.return_book()

    if result[1] > 0:
       # messagebox.showinfo('Success', "Book returned successfully")
        MyMessageBox().showMessage("Book returned successfully", "Success", 1)
    else:
        messagebox.showinfo('Failed', "Operation failed")

    returnView.destroy()


def returnBook():
    global bookInfo1, bookInfo2, SubmitBtn, quitBtn, Canvas1, cur, returnView, labelFrame, lb1

    def onselect(event):
        selected = (listbox2.get(listbox2.curselection()))

        info = selected.split("    ")
        bookInfo1.insert(END, info[0].strip())
        bookInfo2.insert(END, info[1].strip())
        bookInfo3.insert(END, info[2].strip())

    returnView = Tk()
    returnView.title("Library Management System")
    returnView.minsize(width=400, height=400)
    returnView.geometry("600x500")

    Canvas1 = Canvas(returnView)

    Canvas1.config(bg="light green")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(returnView, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    lb1 = Label(returnView, text="Select the book to return from the list ", bg='black', fg='white',
                font=('Courier', 12))
    lb1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.08)

    listbox2 = Listbox(returnView, bg='white')
    listbox2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
    scrollbar2 = Scrollbar(listbox2)
    scrollbar2.pack(side=RIGHT, fill=BOTH)
    issuedbooks = Book()
    curs = issuedbooks.select_issuedbook()

    for values in curs[0]:
        row = values[1] + "     " + values[2] + "     " + values[0].strftime("%d-%m-%Y")
        listbox2.insert(END, row)

    listbox2.config(yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=listbox2.yview)
    listbox2.bind("<<ListboxSelect>>", onselect)

    labelFrame = Frame(returnView, bg='black')
    labelFrame.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.2)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.3)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.3, relwidth=0.62)

    # issued date
    lb2 = Label(labelFrame, text="Member_id : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.5, relwidth=0.62)

    # issued date
    lb3 = Label(labelFrame, text="Issued On : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.7)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.7, relwidth=0.62)

    SubmitBtn = Button(returnView, text="Return Book", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(returnView, text="Cancel", bg='#f7f1e3', fg='black', command=returnView.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    returnView.mainloop()
