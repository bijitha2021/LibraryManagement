import psycopg2
from psycopg2 import Error
from tkinter import messagebox


def db_operation(query, arg):
    data = 1
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="password1",
                                      host="localhost",
                                      port="5432",
                                      database="Library")

        cursor = connection.cursor()
        if len(arg):
            records = cursor.execute(query, arg)
        else:
            records = cursor.execute(query)

        record_count = cursor.rowcount
        if "select" in query:
            data = cursor.fetchall()

        connection.commit()




    except (Exception, Error) as error:
        messagebox.showinfo('Error', error)
        data = 0
    finally:
        if connection:
            cursor.close()
            connection.close()

    return data,record_count
