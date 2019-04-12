# This is a bank application by Tkinter in class...

"""                 ********************************************************************** """

import json,time,os,sys         #importing useful libraries....
from random import randint
from getpass import getpass
import tkinter as tk
import sqlite3 as sql

"""    **************************************************************************** """

# creating functions for database
# creating 3 global functions so that we can use them in functions like debit, credit etc.
db = None
cursor = None
data = None
"""After the execution of db_execute_fetch function the value of data will be:

data= ('rahul123',
 'rahul',
 'charan',
 33000,
 '11100011100',
 'rahul456',
 'charan7rahul@gmail.com',
 2147483647)  

 means data will be in tuple form.
 """


def db_connection():
    global db, cursor
    db = sql.connect("data/bank.db")
    cursor = db.cursor()
    try:
        cursor.execute("create table xyz(username varchar(50) not null primary key, first_name varchar(50) not null, last_name varchar(50) not null, balance int(50) not null, account_number varchar(50) not null, password varchar(50) not null, email varchar(50) not null, phone_number int(50) not null ")
    except sql.OperationalError as e:
        pass



def db_execute_fetch(cmd):
    """database ---->>>>> program"""
    global data
    cursor.execute(cmd)
    data = cursor.fetchone()


def db_execute_insert(cmd):
    """database <<<<<<<-------- program"""
    cursor.execute(cmd)
    db.commit()


def db_close():
    global db, cursor, data
    cursor.close()
    db.close()
    db = None
    cursor = None
    data = None


"""*****************************************************************************"""


class Bank:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.minsize(200,200)
        self.root.wm_iconbitmap("static/icons/piggy-bank.png")
        self.root.config(background="grey")
        self.root.title("XYZ Bank")
        self.username = tk.StringVar()
        self.password = tk.StringVar()


    def menu(self):
        self.menu_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
        self.menu_frame.pack(side="top", pady=150)

        self.menu_label1 = tk.Label(self.menu_frame, text="Welcome To The XYZ Bank", bg='blue', font="times 35 bold")
        self.menu_label1.grid(row=0, column=0, padx=10, columnspan=3)

        self.menu_label2 = tk.Label(self.menu_frame, text="Username: ", font="times 20 bold")
        self.menu_label2.grid(row=1, column=1, padx=10, pady=10)

        self.menu_label3 = tk.Label(self.menu_frame, text="Password: ", font="times 20 bold")
        self.menu_label3.grid(row=2, column=1, padx=10, pady=10)

        self.menu_entry1 = tk.Entry(self.menu_frame, textvariable=self.username)
        self.menu_entry1.grid(row=1, column=2)

        self.menu_entry2 = tk.Entry(self.menu_frame, textvariable=self.password)
        self.menu_entry2.grid(row=2, column=2)

        self.menu_button1 = tk.Button(self.menu_frame, text='Login', fg='blue', command=self.login, font="times 15 bold")
        self.menu_button1.grid(row=3, column=1,pady=10, padx=10, columnspan=4 )

        self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup, font="times 15 bold")
        self.menu_button2.grid(row=3, column=2, pady=10)




    def login(self):
        self.menu_frame.pack_forget()

        self.login_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
        self.login_frame.pack(side="top", pady=150)

        self.login_label = tk.Label(self.login_frame, text="Welcome To The XYZ Bank", bg='red', font="times 35 bold")
        self.login_label.grid(row=0, column=2, padx=50)

        self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup,
                                      font="times 15 bold")
        self.menu_button2.grid(row=3, column=2, pady=10)
        self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup,
                                      font="times 15 bold")
        self.menu_button2.grid(row=3, column=2, pady=10)
        self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup,
                                      font="times 15 bold")
        self.menu_button2.grid(row=3, column=2, pady=10)
        self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup,
                                      font="times 15 bold")
        self.menu_button2.grid(row=3, column=2, pady=10)


    def signup(self):
        pass







"""******************************************************************************************************"""

if __name__=="__main__":
    window = Bank()
    window.menu()
    window.root.mainloop()



