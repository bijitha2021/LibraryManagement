from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

from MyMessageBox import MyMessageBox
from book_manager import *



def deleteBook():
    
    bcode = bookInfo1.get().upper()
   
    bookdel = Book(bcode.upper())
    res = bookdel.delete_book()
    if res[1] > 0:
       # messagebox.showinfo('Success', "Book deleted Successfully")
       MyMessageBox().showMessage("Book deleted Successfully", "Deleted", 1)
    else:
        messagebox.showinfo('Failed', "Operation failed")

    bookInfo1.delete(0, END)
    deleteView.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,deleteView
    
    deleteView = Tk()
    deleteView.title("Library Management System")
    deleteView.minsize(width=400, height=400)
    deleteView.geometry("600x500")

    
    Canvas1 = Canvas(deleteView)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(deleteView, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(deleteView, bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.2)
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white', font=('Courier', 12))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(deleteView, text="Delete Book", bg='#d1ccc0', fg='black', command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.6, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(deleteView, text="Cancel", bg='#f7f1e3', fg='black', command=deleteView.destroy)
    quitBtn.place(relx=0.53,rely=0.6, relwidth=0.18,relheight=0.08)
    
    deleteView.mainloop()