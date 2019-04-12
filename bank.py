# This is a bank application by Tkinter in class...

""" ************************************************************************************************************* """

import json,time,os,sys         #importing useful libraries....
from random import randint
from getpass import getpass
import tkinter as tk
import sqlite3 as sql
import tkinter.messagebox as tmsg

"""    ******************************************************************************************************************** """

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
        cursor.execute("create table xyz(username varchar(50) not null primary key, first_name varchar(50) not null, last_name varchar(50) not null, balance int(50) not null, account_number varchar(50) not null, password varchar(50) not null, email varchar(50) not null, phone_number int(50) not null) ")
        cursor.execute("insert into xyz values('rahul123', 'Rahul', 'Charan', 20000, 11100011101, 'rahul456', 'charan7rahul@gmail.com', 7296925650)")
        db.commit()
    except Exception as e:
        pass
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


"""********************************************************************************************************************"""


class Bank:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.minsize(200,200)
        self.root.wm_iconbitmap("static/icons/piggy-bank.png")
        self.root.config(background="grey")
        self.root.title("XYZ Bank")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.amount = tk.StringVar()

    """  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX """

    def menu(self):

        try:
            self.menu_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
            self.menu_frame.pack(side="top", pady=150)

            self.menu_label1 = tk.Label(self.menu_frame, text="Welcome To The XYZ Bank", bg='blue', font="times 35 bold")
            self.menu_label1.grid(row=0, column=0, padx=10, columnspan=3)

            self.menu_label2 = tk.Label(self.menu_frame, text="Username: ", font="times 20 bold")
            self.menu_label2.grid(row=1, column=1, padx=10, pady=10)

            self.menu_entry1 = tk.Entry(self.menu_frame, textvariable=self.username)
            self.menu_entry1.grid(row=1, column=2)

            self.menu_label3 = tk.Label(self.menu_frame, text="Password: ", font="times 20 bold")
            self.menu_label3.grid(row=2, column=1, padx=10, pady=10)

            self.menu_entry2 = tk.Entry(self.menu_frame, textvariable=self.password, show='*')
            self.menu_entry2.grid(row=2, column=2)

            self.menu_button1 = tk.Button(self.menu_frame, text='Login', fg='blue', command=self.login, font="times 15 bold")
            self.menu_button1.grid(row=3, column=1,pady=10, padx=10, columnspan=4 )

            self.menu_button2 = tk.Button(self.menu_frame, text='Signup', fg='blue', command=self.signup, font="times 15 bold")
            self.menu_button2.grid(row=3, column=2, pady=10)


        except Exception as e:
            tmsg.showerror("Error", e)


    """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx """


    def login(self):


        db_connection()
        cmd = f"select * from xyz where username='{self.username.get()}'"
        db_execute_fetch(cmd)

        if data:
            if self.password.get() == data[5]:
                self.menu_frame.pack_forget()

                self.login_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
                self.login_frame.pack(side="top", pady=150)

                self.login_label = tk.Label(self.login_frame, text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='red',font="times 35 bold")
                self.login_label.grid(row=0, column=0, columnspan=3)

                self.login_button1 = tk.Button(self.login_frame, text='Debit', fg='blue', command=self.debit,
                                               font="times 15 bold")
                self.login_button1.grid(row=2, column=0, pady=10)

                self.login_button2 = tk.Button(self.login_frame, text='Credit', fg='blue', command=self.credit,
                                               font="times 15 bold")
                self.login_button2.grid(row=2, column=1, pady=10)

                self.login_button3 = tk.Button(self.login_frame, text='Check Balance', fg='blue',
                                               command=self.check_balance,
                                               font="times 15 bold")
                self.login_button3.grid(row=3, column=0, pady=10)

                self.login_button4 = tk.Button(self.login_frame, text='Profile', fg='blue', command=self.profile,
                                               font="times 15 bold")
                self.login_button4.grid(row=3, column=1, pady=10)

                self.login_button5 = tk.Button(self.login_frame, text='Logout', fg='blue', command=self.logout,
                                               font="times 15 bold")
                self.login_button5.grid(row=4, column=0, pady=10, columnspan=2)

            else:
                tmsg.showinfo("Login", "Incorrect Password  !!!!!!!!")

        else:
            tmsg.showinfo(title='Login',message="User Does Not Exist...Please Enter Correct Username.......")



    """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def debit(self):
        self.login_frame.pack_forget()

        self.debit_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
        self.debit_frame.pack(side="top", pady=150)

        self.debit_label = tk.Label(self.debit_frame,
                                    text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='red',
                                    font="times 35 bold")
        self.debit_label.grid(row=0, column=0, columnspan=3)

        self.debit_label2 = tk.Label(self.debit_frame, text="Amount: ", font="times 20 bold")
        self.debit_label2.grid(row=1, column=1, padx=10, pady=10)

        self.debit_entry1 = tk.Entry(self.debit_frame, textvariable=self.amount)
        self.debit_entry1.grid(row=1, column=2)

        self.debit_button1 = tk.Button(self.debit_frame, text='Submit', fg='blue', command=self.debit_submit,
                                      font="times 15 bold")
        self.debit_button1.grid(row=3, column=2, pady=10, padx=10, columnspan=4)

        self.debit_button2 = tk.Button(self.debit_frame, text='<<--Back', fg='blue', command=self.back_debit,
                                      font="times 15 bold")
        self.debit_button2.grid(row=3, column=0, pady=10, columnspan=1)


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"""

    def debit_submit(self):
        try:
            extra_amount = int(self.amount.get())
            if data[3] > extra_amount:
                new_amount = data[3] - extra_amount
                cmd1 = f"update xyz set balance='{new_amount}' where username='{self.username.get()}' "
                db_execute_insert(cmd1)

                tmsg.showinfo("Debit", f"Amount Rs {extra_amount} is Debitted From Your Account...")

                self.debit_frame.pack_forget()
                self.login()

            else:
                tmsg.showinfo("Debit", "You Do Not Have Sufficient Amount....Please Enter Less Amount.....")

        except ValueError as e:
            tmsg.showerror("Error", "ERROR-->>> Only Enter Numbers Not Alphabet And Do Not Leave It Blank...")

        except Exception as e:
            tmsg.showerror("Error", e)

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def back_debit(self):

        self.debit_frame.pack_forget()

        self.login()

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def credit(self):

        self.login_frame.pack_forget()

        self.credit_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
        self.credit_frame.pack(side="top", pady=150)

        self.credit_label = tk.Label(self.credit_frame,
                                    text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='red',
                                    font="times 35 bold")
        self.credit_label.grid(row=0, column=0, columnspan=3)

        self.credit_label2 = tk.Label(self.credit_frame, text="Amount: ", font="times 20 bold")
        self.credit_label2.grid(row=1, column=1, padx=10, pady=10)

        self.credit_entry1 = tk.Entry(self.credit_frame, textvariable=self.amount)
        self.credit_entry1.grid(row=1, column=2)

        self.credit_button1 = tk.Button(self.credit_frame, text='Submit', fg='blue', command=self.credit_submit,
                                       font="times 15 bold")
        self.credit_button1.grid(row=3, column=2, pady=10, padx=10, columnspan=4)

        self.credit_button2 = tk.Button(self.credit_frame, text='<<--Back', fg='blue', command=self.back_credit,
                                       font="times 15 bold")
        self.credit_button2.grid(row=3, column=0, pady=10, columnspan=1)

        """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def credit_submit(self):

        try:
            extra_amount = int(self.amount.get())
            new_amount = data[3] + extra_amount
            cmd1 = f"update xyz set balance='{new_amount}' where username='{self.username.get()}' "
            db_execute_insert(cmd1)

            tmsg.showinfo("Credit", f"Amount Rs {extra_amount} is Deposited Successfuly...")

            self.credit_frame.pack_forget()
            self.login()

        except Exception as e:
            tmsg.showerror("Error", "ERROR--->>> Please Enter Amount And then Press submit ")

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def back_credit(self):
        self.credit_frame.pack_forget()

        self.login()


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"""

    def check_balance(self):
        tmsg.showinfo("Balance", f"Your Account Balance is --->>>>  Rs {data[3]}")


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def profile(self):

        self.login_frame.pack_forget()

        self.profile_frame = tk.Frame(self.root, bg='lightblue', relief='sunken', borderwidth=9)
        self.profile_frame.pack(side="top", pady=100)

        self.profile_label = tk.Label(self.profile_frame, text="***Your Profile Details***", bg='blue', font="times 30 bold")
        self.profile_label.grid(row=0, column=0, padx=10, columnspan=3)

        self.profile_label1 = tk.Label(self.profile_frame, text="Username: ", font="times 20 bold")
        self.profile_label1.grid(row=1, column=0, padx=10, pady=10)

        self.profile_label11 = tk.Label(self.profile_frame, text=f"{data[0]} ", font="times 20 bold")
        self.profile_label11.grid(row=1, column=1, padx=10, pady=10)

        self.profile_label2 = tk.Label(self.profile_frame, text="Name: ", font="times 20 bold")
        self.profile_label2.grid(row=2, column=0, padx=10, pady=10)

        self.profile_label22 = tk.Label(self.profile_frame, text=f"{data[1]} ", font="times 20 bold")
        self.profile_label22.grid(row=2, column=1, padx=10, pady=10)

        self.profile_label3 = tk.Label(self.profile_frame, text="Balance: ", font="times 20 bold")
        self.profile_label3.grid(row=3, column=0, padx=10, pady=10)

        self.profile_label33 = tk.Label(self.profile_frame, text=f"Rs {data[3]} ", font="times 20 bold")
        self.profile_label33.grid(row=3, column=1, padx=10, pady=10)

        self.profile_label4 = tk.Label(self.profile_frame, text="Account_Number: ", font="times 20 bold")
        self.profile_label4.grid(row=4, column=0, padx=10, pady=10)

        self.profile_label44 = tk.Label(self.profile_frame, text=f"{data[4]} ", font="times 20 bold")
        self.profile_label44.grid(row=4, column=1, padx=10, pady=10)

        self.profile_label5 = tk.Label(self.profile_frame, text="Email: ", font="times 20 bold")
        self.profile_label5.grid(row=5, column=0, padx=10, pady=10)

        self.profile_label55 = tk.Label(self.profile_frame, text=f"{data[6]} ", font="times 20 bold")
        self.profile_label55.grid(row=5, column=1, padx=10, pady=10)

        self.profile_label6 = tk.Label(self.profile_frame, text="Phone_Number: ", font="times 20 bold")
        self.profile_label6.grid(row=6, column=0, padx=10, pady=10)

        self.profile_label66 = tk.Label(self.profile_frame, text=f"{data[7]} ", font="times 20 bold")
        self.profile_label66.grid(row=6, column=1, padx=10, pady=10)

        self.profile_button1 = tk.Button(self.profile_frame, text='<<--Back', fg='blue', command=self.back_profile,
                                        font="times 15 bold")
        self.profile_button1.grid(row=7, column=0)

        # One can use for loop here also.



    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def back_profile(self):
        self.profile_frame.pack_forget()

        self.login()


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def logout(self):
        self.login_frame.pack_forget()
        self.menu()
        self.username.set('')
        self.password.set('')


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def signup(self):
        pass







"""***********************************************************************************************************************"""

if __name__=="__main__":
    window = Bank()
    window.menu()
    window.root.mainloop()



