from tkinter import *


class MyMessageBox:

    def __init__(self):
        self.returnValue = 0
        self.myMessageBox = Tk()

    def showMessage(self, msg, title, type):

        if title is None:
            title = "Library Management System"
        self.myMessageBox.title(title)
        self.myMessageBox.geometry("300x100+300+300")
        self.myMessageBox.configure(bg='light blue')
        headingLabel = Label(self.myMessageBox, text=msg, bg='light blue', fg='red', font=('Courier', 10))
        headingLabel.place(relx=0.1, rely=0.3, relwidth=0.7, relheight=0.2)
        if type == 2:

            okBtn = Button(self.myMessageBox, text="Ok", bg='#f7f1e3', fg='black', command=self.okOperation(1))
            okBtn.place(relx=0.2, rely=0.7, relwidth=0.2, relheight=0.2)
        cancelBnt = Button(self.myMessageBox, text="Ok", bg='#f7f1e3', fg='black', command=self.cancelOperation)
        cancelBnt.place(relx=0.4, rely=0.7, relwidth=0.3, relheight=0.2)
        return self.returnValue

    def cancelOperation(self):
        self.returnValue = 0
        self.myMessageBox.destroy()
        return self.returnValue

    def okOperation(self, y):
        self.returnValue = y
        self.myMessageBox.destroy()
        return self.returnValue
