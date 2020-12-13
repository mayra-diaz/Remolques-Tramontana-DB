
import tkinter as tk
from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
import psycopg2


def connection():
    return psycopg2.connect(
        dbname="Koob",
        user="postgres",
        password="maor&roizman30",
        host="localhost",
        port="5432"
    )

#Funciones

def buscar_libro_isbn(isbn):
    conn = connection()
    cursor = conn.cursor()
    query = f"""
    SELECT pbe.book_name as book, pbe.ed_name as editorial, CONCAT(a.first_name,' ',a.last_name) as author FROM
(SELECT pb.book_name, e.ed_name, pb.auth_id FROM
(SELECT p.book_name, p.ed_id, p.auth_id from
(SELECT book_name, ed_id, auth_id FROM koob.publishes1000 WHERE isbn = '{isbn}') p
INNER JOIN
(SELECT book_name, ed_id, auth_id FROM koob.books1000) b
ON p.book_name = b.book_name AND p.ed_id = b.ed_id AND p.auth_id = b.auth_id) pb
INNER JOIN
(SELECT ed_id, ed_name FROM koob.editorials1000) e
on e.ed_id = pb.ed_id) pbe
INNER JOIN
(SELECT first_name, last_name, auth_id FROM koob.authors1000) a
ON a.auth_id = pbe.auth_id;"""

    cursor.execute(query)
    
    row = cursor.fetchall()
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10,columnspan=4, sticky=W+E)

    for book in row:
        listbox.insert(END, book)

    conn.commit()
    conn.close()

def buscar_libro_title(title):
    conn = connection()
    cursor = conn.cursor()
    query = f" SELECT * FROM koob.books1000 WHERE book_name like '%{title}%' "
    cursor.execute(query)
    
    row = cursor.fetchall()
    listbox = Listbox(frame, width=100, height=5)
    listbox.grid(row=10,columnspan=4, sticky=W+E)

    for book in row:
        listbox.insert(END, book)

    conn.commit()
    conn.close()

def buscar_libro(isbn, author, title):
    conn = connection()
    cursor = conn.cursor()

    if(isbn != ""):
        query = " SELECT * FROM koob.books1000 "
    elif(author != ""):
        query = f" SELECT * FROM koob.books1000 WHERE book_name like '%{title}%' "
    elif(title != ""):
        query = f" SELECT * FROM koob.books1000 WHERE book_name like '%{title}%' "


    cursor.execute(query)
    
    row = cursor.fetchall()
    listbox = Listbox(frame, width=100, height=5)
    listbox.grid(row=10,columnspan=4, sticky=W+E)

    for book in row:
        listbox.insert(END, book)

    conn.commit()
    conn.close()


window = Tk()
window.title("®Koob - Interfaz de administrador")


#Canvas
canvas = Canvas(window, height=600, width=600)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text ='Buscar un libro')

#ISBN
label_isbn = Label(frame, text="ISBN: ")
label_isbn.grid(row=1, column=0)
entry_isbn = Entry(frame)
entry_isbn.grid(row=1, column=1)

#AUTOR
label_author = Label(frame, text="Author: ")
label_author.grid(row=2, column=0)
entry_author = Entry(frame)
entry_author.grid(row=2, column=1)

#TITULO
label_title = Label(frame, text="Title: ")
label_title.grid(row=3, column=0)
entry_title = Entry(frame)
entry_title.grid(row=3, column=1)


# BOTON
button = Button(frame, text="Buscar", command=lambda:buscar_libro(
    entry_isbn.get(),
    entry_author.get(),
    entry_title.get()
    ))
button.grid(row=4,column=1,sticky=W+E)


window.mainloop()