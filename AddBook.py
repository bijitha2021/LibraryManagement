from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from book_manager import *

#subin added comment
def bookRegister():
    bcode = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = "Available"

    bookadd = Book(bcode.upper(), title.upper(), author.upper(), status)
    res = bookadd.add_book()

    addView.destroy()

    if res[1] > 0:
        messagebox.showinfo('Success', "Book added Successfully")
    else:
        messagebox.showinfo('Failed', "Operation failed")


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, addView

    addView = Toplevel()
    addView.title("Library Management System")
    addView.minsize(width=400, height=400)
    addView.geometry("600x500")

    img2 = (Image.open("add.png"))
    resized_image2 = img2.resize((600, 550), Image.ANTIALIAS)
    new_image2 = ImageTk.PhotoImage(resized_image2)

    Canvas1 = Canvas(addView)

    Canvas1.config(bg="light yellow")
    Canvas1.pack(expand=True, fill=BOTH)
    Canvas1.create_image(10, 10, anchor=NW, image=new_image2)

    headingFrame1 = Frame(addView, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(addView, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    lb1 = Label(labelFrame, text="Book Code : ", bg='black', fg='white', font=('Courier', 12))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white', font=('Courier', 12))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(addView, text="Add Book", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

    quitBtn = Button(addView, text="Cancel", bg='#f7f1e3', fg='black', command=addView.destroy)
    quitBtn.place(relx=0.53, rely=0.7, relwidth=0.18, relheight=0.08)

    addView.mainloop()
