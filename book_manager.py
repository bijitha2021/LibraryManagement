from connection import *


class Book:

    def __init__(self, code=None, title=None, author=None, status=None, member_id=None, issue_date=None):
        self.code = code
        self.title = title
        self.author = author
        self.status = status
        self.member_id = member_id
        self.issue_date = issue_date

    # To add book to database
    def add_book(self):
        str_query = """ INSERT INTO books (code, title,author,status) VALUES (%s,%s,%s,%s)"""

        query_arg = (self.code, self.title, self.author, self.status)

        result = db_operation(str_query, query_arg)

        return result

    # To delete the book
    def delete_book(self):
        del_query = """delete from books  where code = %s"""

        query_arg = (self.code,)

        result = db_operation(del_query, query_arg)

        return result

    def select_book(self):
        sel_query = """select code,title,author,status from books  where status = %s"""

        query_arg = (self.status,)

        result = db_operation(sel_query, query_arg)

        return result

    # Update book status
    def update_book(self):
        str_query = """ update books set status = %s where code =%s"""

        query_arg = (self.status, self.code)

        result = db_operation(str_query, query_arg)

        return result

    # To issue a book to a member
    def issue_book(self):
        issue_query = """ INSERT INTO book_issue (code, member_id,issue_date) VALUES (%s,%s,%s)"""

        query_arg = (self.code, self.member_id, self.issue_date)

        result = db_operation(issue_query, query_arg)
        self.status = "Issued"
        self.update_book()

        return result

    def select_issuedbook(self):
        sel_query = """select issue_date,code,member_id from book_issue where issue_return isnull order by issue_date"""
        args = ""
        result = db_operation(sel_query, args)

        return result

    # when books are returned
    def return_book(self):
        str_query = """ update books set status ='Available' where code =%s"""

        query_arg = (self.code,)

        result = db_operation(str_query, query_arg)
        str_query = """delete from book_issue  where code = %s and member_id = %s """

        query_arg = (self.code, self.member_id)

        result = db_operation(str_query, query_arg)
        return result

    def search_book(self):
        if self.author is not None:

            sel_query = """select code,title,author,status from books  where author like upper(%s)"""
            query_arg = ('%' + self.author + '%',)

        elif self.title is not None:
            sel_query = """select code,title,author,status from books  where title like upper(%s)"""
            query_arg = ('%' + self.title + '%',)

        result = db_operation(sel_query, query_arg)

        return result
