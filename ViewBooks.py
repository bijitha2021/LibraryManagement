from tkinter import ttk
from IssueBook import *
from book_manager import Book
from MyMessageBox import MyMessageBox
from stringtrim import str_format
import re


def View():
    global bookcombo, curs, val
    status = "Available"

    def booksearch():
        listbox1.delete(0, END)
        if bookcombo.get() == "Author":
            viewbook = Book(author=booksearch1.get())
            curs = viewbook.search_book()
        elif bookcombo.get() == "Title":
            viewbook = Book(title=booksearch1.get())
            curs = viewbook.search_book()
        else:
            viewbook = Book(status="Available")
            curs = viewbook.select_book()

        for values in curs[0]:
            row = str_format(values[0], 10) + " \t " + str_format(values[1], 40) + " \t " + str_format(values[2],
                                                                                                       15) + " \t " + "(" + \
                  values[3] + ")"

            listbox1.insert(END, row)

    def onselect(event):
        selected = (listbox1.get(listbox1.curselection()))
        # info=re.split('[\t,][\t,]',selected)
        info = selected.split("\t")

        if len(info[3]) and info[3].strip() == "(Issued)":
            # messagebox.showinfo('Not', "This Book is not available")
            # myMessage = MyMessageBox()

            msg = MyMessageBox()
            v1 = msg.showMessage("This Book issued already", "Book not available", 1)
            # v1 = MyMessageBox().showMessage("This Book issued already", "Book not available", 2)

        else:
            issueBook(info[0].strip())
            booksView.destroy()

    booksView = Tk()
    booksView.title("Library Management System")
    booksView.minsize(width=400, height=400)
    booksView.geometry("600x500")

    Canvas1 = Canvas(booksView)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(booksView, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    booksearch1 = Entry(booksView)
    booksearch1.place(relx=0.2, rely=0.3, relwidth=0.3, relheight=0.05)

    lb1 = Label(booksView, text="Search By:", bg='#12a4d9', fg='Black')
    lb1.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.05)

    bookcombo = ttk.Combobox(booksView, values=["Author", "Title"])
    bookcombo.current(1)
    bookcombo.place(relx=0.6, rely=0.3, relwidth=0.1, relheight=0.05)

    searchBtn = Button(booksView, text="Search", bg='#f7f1e3', fg='black', command=booksearch)
    searchBtn.place(relx=0.7, rely=0.3, relwidth=0.1, relheight=0.05)

    listbox1 = Listbox(booksView, bg='white')
    listbox1.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
    scrollbar1 = Scrollbar(listbox1)
    scrollbar1.pack(side=RIGHT, fill=BOTH)

    viewbook = Book(status="Available")
    curs = viewbook.select_book()

    if curs is not None:

        for values in curs[0]:
            row = str_format(values[0], 10) + " \t " + str_format(values[1], 40) + " \t " + str_format(values[2],
                                                                                                       15) + " \t" + "(" + \
                  values[3] + ")"

            listbox1.insert(END, row)

    listbox1.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=listbox1.yview)
    listbox1.bind("<<ListboxSelect>>", onselect)

    quitBtn = Button(booksView, text="Cancel", bg='#f7f1e3', fg='black', command=booksView.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    booksView.mainloop()
