from datetime import date
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from MyMessageBox import MyMessageBox
from book_manager import Book


def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, issueView, Canvas1, status

    bcode = inf1.get().upper().strip()
    issueto = inf2.get().upper().strip()
    date_issue = date.today()


    if len(issueto):

        bookissue = Book(bcode, member_id = issueto, issue_date = date_issue)
        res = bookissue.issue_book()

        if res[1] > 0:
            #messagebox.showinfo('Success', "Book issued")
            MyMessageBox().showMessage("Book issued Successfully", "issued", 1)
        else:
            messagebox.showinfo('Failed', "Operation failed")

        issueView.destroy()
    else:
        messagebox.showinfo('Enter', "Enter Member_id")


def issueBook(code):
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, issueView, Canvas1, status



    issueView = Toplevel()
    issueView.title("Library Management System")
    issueView.minsize(width=400, height=400)
    issueView.geometry("600x500")

    img2 = (Image.open("view.png"))
    resized_image2 = img2.resize((600, 550), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(resized_image2)

    Canvas1 = Canvas(issueView)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)
    Canvas1.create_image(10, 10, anchor=NW, image=new_image2)

    headingFrame1 = Frame(issueView, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(issueView, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)
    inf1.insert(END, code)

    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    issueBtn = Button(issueView, text="Issue Book", bg='#d1ccc0', fg='black', command=issue)
    issueBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

    quitBtn = Button(issueView, text="Cancel", bg='#aaa69d', fg='black', command=issueView.destroy)
    quitBtn.place(relx=0.53, rely=0.7, relwidth=0.18, relheight=0.08)

    issueView.mainloop()
