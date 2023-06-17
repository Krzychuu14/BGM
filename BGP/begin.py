import tkinter as tk
from tkinter import ttk
import sqlite3

import database
import main

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

database.persons(conn, cursor)
database.moves(conn, cursor)
database.combined_table(conn, cursor)
# database.(conn, cursor)

def change_windows():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    firstName = name_entry.get()
    lastName = surname_entry.get()
    age = age_spinbox.get()

    cursor.execute("INSERT INTO persons(fName, sName, age) VALUES(?,?,?)", (firstName, lastName, age))
    conn.commit()
    conn.close()

    root.destroy()
    main.app.mainloop()

def delete_history():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM combined_table")

    conn.commit()
    conn.close()

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

root = tk.Tk()

style = ttk.Style(root)
root.tk.call('source', 'forest-light.tcl')
style.theme_use('forest-light')

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text='Insert Row')
widgets_frame.grid(row=0, column=0, padx=20, pady=10)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, 'First Name')  # Napis wewnącz miejsca na wpisanie
name_entry.bind('<FocusIn>', lambda e: name_entry.delete('0', 'end'))   # Usunięcie napisu w środku
name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky='ew')

surname_entry = ttk.Entry(widgets_frame)
surname_entry.insert(0, 'Surname')  # Napis wewnącz miejsca na wpisanie
surname_entry.bind('<FocusIn>', lambda e: surname_entry.delete('0', 'end'))   # Usunięcie napisu w środku
surname_entry.grid(row=1, column=0, padx=5, pady=(0, 5), sticky='ew')

age_spinbox = ttk.Spinbox(widgets_frame, from_=0, to=150)
age_spinbox.insert(0, 'Age')
age_spinbox.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

button = ttk.Button(widgets_frame, text="Find Video", command=change_windows)
button.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

seperator = ttk.Separator(widgets_frame)
seperator.grid(row=4, column=0, padx=(20, 10), pady=10, sticky='ew')

button = ttk.Button(widgets_frame, text="Delete History", command=delete_history)
button.grid(row=5, column=0, padx=5, pady=10, sticky='nsew')


# Historia
cursor.execute("SELECT fName, sName, age, name, link FROM combined_table ORDER BY idP DESC")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=15)
treeScroll = ttk.Scrollbar(treeFrame)   # Dodajemy możliwość scrolowania tabeli
treeScroll.pack(side='right', fill='y')

cols = ('fName', 'sName', 'age', 'name', 'link')
treeview = ttk.Treeview(treeFrame, show='headings', yscrollcommand=treeScroll.set, columns=cols, height=10)    # Chcemy wyświetlić tylko 13 wierszy

treeview.column('fName', width=75)
treeview.column('sName', width=75)
treeview.column('age', width=30)
treeview.column('name', width=100)
treeview.column('link', width=100)

# Wyświetlamy nazwy kolumn (szare pole)
treeview.heading('fName', text='First name')
treeview.heading('sName', text='Last name')
treeview.heading('age', text='Age')
treeview.heading('name', text='Name of video')
treeview.heading('link', text='Link to YT')

i = 0
for record in cursor:
    treeview.insert('', i, text='', value=(record[0], record[1], record[2], record[3], record[4]))
    i += 1

treeview.pack()
treeScroll.config(command=treeview.yview)


conn.commit()
conn.close()

root.mainloop()