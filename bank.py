# This is a bank application by Tkinter in class...

""" ************************************************************************************************************* """

import json,time,os,sys         #importing useful libraries....
from random import randint
import tkinter as tk
import sqlite3 as sql
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk

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
    db.commit()
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
        self.root.geometry("700x600")
        self.root.minsize(200,200)
        self.root.wm_iconbitmap("static/icons/5.ico")
        self.root.config(background="#FFDAB9")
        self.root.title("XYZ Bank")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.amount = tk.StringVar()
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.verify_password = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_number = tk.StringVar()


        self.old_password = tk.StringVar()
        self.new_password = tk.StringVar()
        self.verify_new_password = tk.StringVar()
        self.new_first_name = tk.StringVar()
        self.new_last_name = tk.StringVar()
        self.new_email = tk.StringVar()
        self.new_phone_number = tk.StringVar()





    """  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX """

    def image_insert(self):
        try:

            self.image1 = Image.open("static/images/3.jpg")
            self.photo1 = ImageTk.PhotoImage(self.image1)

            self.image_label1 = tk.Label(self.root, image=self.photo1)
            self.image_label1.pack(side='left', anchor='nw')

            self.image2 = Image.open("static/images/6.jpg")
            self.photo2 = ImageTk.PhotoImage(self.image2)

            self.image_label2 = tk.Label(self.root, image=self.photo2)
            self.image_label2.place(x=400, y=550)

            self.image3 = Image.open("static/images/8.jpg")
            self.photo3 = ImageTk.PhotoImage(self.image3)

            self.image_label3 = tk.Label(self.root, image=self.photo3)
            self.image_label3.place(x=400, y=0)

            self.image4 = Image.open("static/images/10.jpg")
            self.photo4 = ImageTk.PhotoImage(self.image4)

            self.image_label4 = tk.Label(self.root, image=self.photo4)
            self.image_label4.place(x=1000, y=0)

            self.image5 = Image.open("static/images/12.jpg")
            self.photo5 = ImageTk.PhotoImage(self.image5)

            self.image_label5 = tk.Label(self.root, image=self.photo5)
            self.image_label5.place(x=800, y=400)

            self.image6 = Image.open("static/images/14.jpg")
            self.photo6 = ImageTk.PhotoImage(self.image6)

            self.image_label6 = tk.Label(self.root, image=self.photo6)
            self.image_label6.place(x=400, y=400)


        except Exception as e:
            tmsg.showerror('Error', e)

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def image_delete(self):
        try:

            self.image_label1.pack_forget()
            self.image_label2.place_forget()
            self.image_label3.place_forget()
            self.image_label4.place_forget()
            self.image_label5.place_forget()
            self.image_label6.place_forget()

        except Exceptionas e:
            tmsg.showerror('Error',e)



    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def menu(self):

        try:

            self.image_insert()

            self.menu_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
            self.menu_frame.pack(side="top", pady=150)

            self.menu_label = tk.Label(self.root, text="****By Rahul Charan****", bg='#4169E1',
                                       font="times 25 italic")
            self.menu_label.pack(side='bottom', anchor='se')



            self.menu_label1 = tk.Label(self.menu_frame, text="**Welcome To The XYZ Bank**", bg='#FFA07A', font="times 35 bold")
            self.menu_label1.grid(row=0, column=0, padx=10, columnspan=3)

            self.menu_label2 = tk.Label(self.menu_frame, text="Username: ", font="times 20 bold")
            self.menu_label2.grid(row=1, column=1, padx=10, pady=10)

            self.menu_entry1 = tk.Entry(self.menu_frame, textvariable=self.username)
            self.menu_entry1.grid(row=1, column=2)

            self.menu_label3 = tk.Label(self.menu_frame, text="Password: ", font="times 20 bold")
            self.menu_label3.grid(row=2, column=1, padx=10, pady=10)

            self.menu_entry2 = tk.Entry(self.menu_frame, textvariable=self.password, show='*')
            self.menu_entry2.grid(row=2, column=2)

            self.menu_button1 = tk.Button(self.menu_frame, text='*Login*', fg='blue', command=self.login, font="times 15 bold")
            self.menu_button1.grid(row=3, column=1,pady=10, padx=10, columnspan=4 )

            self.menu_button2 = tk.Button(self.menu_frame, text='*Signup*', fg='blue', command=self.signup, font="times 15 bold")
            self.menu_button2.grid(row=3, column=2, pady=10)



        except Exception as e:
            tmsg.showerror("Error", e)


    """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx """


    def login(self):

        try:
            db_connection()
            cmd = f"select * from xyz where username='{self.username.get()}'"
            db_execute_fetch(cmd)

            if data:
                if self.password.get() == data[5]:
                    self.menu_frame.pack_forget()


                    self.login_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
                    self.login_frame.pack(side="top", pady=150)

                    self.login_label = tk.Label(self.login_frame, text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='#FFA07A',font="times 35 bold")
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

                    self.login_button5 = tk.Button(self.login_frame, text='*Logout*', fg='blue', command=self.logout,
                                                   font="times 15 bold")
                    self.login_button5.grid(row=4, column=0, pady=10, columnspan=2)

                    self.login_button6 = tk.Button(self.login_frame, text='Setting', fg='blue', command=self.setting,
                                                   font="times 15 bold")
                    self.login_button6.grid(row=2, column=2, pady=10)


                else:
                    tmsg.showinfo("Login", "Incorrect Password  !!!!!!!!")

            else:
                tmsg.showinfo(title='Login',message="User Does Not Exist...Please Enter Correct Username.......")


        except Exception as e:
            tmsg.showerror('Error', f'Error--->>>   {e}')



    """ XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def debit(self):

        try:
            self.login_frame.pack_forget()

            self.debit_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
            self.debit_frame.pack(side="top", pady=150)

            self.debit_label = tk.Label(self.debit_frame,
                                        text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='#FFA07A',
                                        font="times 35 bold")
            self.debit_label.grid(row=0, column=0, columnspan=3)

            self.debit_label2 = tk.Label(self.debit_frame, text="Amount: ", font="times 20 bold")
            self.debit_label2.grid(row=1, column=1, padx=10, pady=10)

            self.debit_entry1 = tk.Entry(self.debit_frame, textvariable=self.amount)
            self.debit_entry1.grid(row=1, column=2)

            self.debit_button1 = tk.Button(self.debit_frame, text='*Update*', fg='blue', command=self.debit_submit,
                                          font="times 15 bold")
            self.debit_button1.grid(row=3, column=2, pady=10, padx=10, columnspan=4)

            self.debit_button2 = tk.Button(self.debit_frame, text='<<<--Back', fg='blue', command=self.back_debit,
                                          font="times 15 bold")
            self.debit_button2.grid(row=3, column=0, pady=10, columnspan=1)


        except Exception as e:
            tmsg.showerror('Error', f'Error--->>> {e}')


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"""

    def debit_submit(self):
        try:
            extra_amount = int(self.amount.get())
            if data[3] > extra_amount:
                new_amount = data[3] - extra_amount
                cmd1 = f"update xyz set balance='{new_amount}' where username='{self.username.get()}' "
                db_execute_insert(cmd1)

                tmsg.showinfo("Debit", f"Amount Rs {extra_amount} is Debitted From Your Account...")

                self.amount.set('')
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

        try:

            self.login_frame.pack_forget()

            self.credit_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
            self.credit_frame.pack(side="top", pady=150)

            self.credit_label = tk.Label(self.credit_frame,
                                        text=f"Welcome {data[1].title()} {data[2].title()} To The XYZ Bank", bg='#FFA07A',
                                        font="times 35 bold")
            self.credit_label.grid(row=0, column=0, columnspan=3)

            self.credit_label2 = tk.Label(self.credit_frame, text="Amount: ", font="times 20 bold")
            self.credit_label2.grid(row=1, column=1, padx=10, pady=10)

            self.credit_entry1 = tk.Entry(self.credit_frame, textvariable=self.amount)
            self.credit_entry1.grid(row=1, column=2)

            self.credit_button1 = tk.Button(self.credit_frame, text='*Update*', fg='blue', command=self.credit_submit,
                                           font="times 15 bold")
            self.credit_button1.grid(row=3, column=2, pady=10, padx=10, columnspan=4)

            self.credit_button2 = tk.Button(self.credit_frame, text='<<<--Back', fg='blue', command=self.back_credit,
                                           font="times 15 bold")
            self.credit_button2.grid(row=3, column=0, pady=10, columnspan=1)


        except Exception as e:
            tmsg.showerror('Error', f'Error--->>>  {e}')

        """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def credit_submit(self):

        try:
            extra_amount = int(self.amount.get())
            new_amount = data[3] + extra_amount
            cmd1 = f"update xyz set balance='{new_amount}' where username='{self.username.get()}' "
            db_execute_insert(cmd1)

            tmsg.showinfo("Credit", f"Amount Rs {extra_amount} is Deposited Successfuly...")

            self.amount.set('')
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

        self.profile_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.profile_frame.pack(side="top", pady=100)

        self.profile_label = tk.Label(self.profile_frame, text="***Your Profile Details***", bg='#FFA07A', font="times 30 bold")
        self.profile_label.grid(row=0, column=0, padx=10, columnspan=3)

        self.profile_label1 = tk.Label(self.profile_frame, text="Username: ", font="times 20 bold")
        self.profile_label1.grid(row=1, column=0, padx=10, pady=10)

        self.profile_label11 = tk.Label(self.profile_frame, text=f"{data[0]} ", font="times 20 bold")
        self.profile_label11.grid(row=1, column=1, padx=10, pady=10)

        self.profile_label2 = tk.Label(self.profile_frame, text="Name: ", font="times 20 bold")
        self.profile_label2.grid(row=2, column=0, padx=10, pady=10)

        self.profile_label22 = tk.Label(self.profile_frame, text=f"{data[1].title()} {data[2].title()}", font="times 20 bold")
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

        self.profile_button1 = tk.Button(self.profile_frame, text='<<<--Back', fg='blue', command=self.back_profile,
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
        self.menu_label.pack_forget()
        self.image_delete()

        self.username.set('')
        self.password.set('')
        self.phone_number.set('')
        self.first_name.set('')
        self.last_name.set('')
        self.email.set('')

        self.menu()

        db_close()



    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def setting(self):

        try:

            self.login_frame.pack_forget()

            self.setting_label_detail = tk.Label(self.root, text="Setting-->>>", bg='blue',
                                              font="times 20 italic")
            self.setting_label_detail.pack(side='top', pady=25)


            self.setting_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
            self.setting_frame.pack(side="top", pady=150)

            self.setting_label = tk.Label(self.setting_frame,
                                        text=f"**What Do You Want To Change**", bg='#FFA07A',
                                        font="times 30 bold")
            self.setting_label.grid(row=0, column=0, columnspan=3)

            self.setting_button1 = tk.Button(self.setting_frame, text='Password', fg='blue', command=self.setting_password,
                                           font="times 15 bold")
            self.setting_button1.grid(row=2, column=0, pady=10)

            self.setting_button2 = tk.Button(self.setting_frame, text='Name', fg='blue', command=self.setting_name,
                                           font="times 15 bold")
            self.setting_button2.grid(row=2, column=1, pady=10)

            self.setting_button3 = tk.Button(self.setting_frame, text='Email', fg='blue',
                                           command=self.setting_email,
                                           font="times 15 bold")
            self.setting_button3.grid(row=3, column=0, pady=10)

            self.setting_button4 = tk.Button(self.setting_frame, text='Phone Number', fg='blue', command=self.setting_phone_number,
                                           font="times 15 bold")
            self.setting_button4.grid(row=3, column=1, pady=10)

            self.setting_button5 = tk.Button(self.setting_frame, text='<<--Back', fg='blue',
                                             command=self.setting_back,
                                             font="times 15 bold")
            self.setting_button5.grid(row=5, column=0, columnspan=2, pady=10)


        except Exception as e:
            tmsg.showerror('Error', f'Error--->>>  {e}')


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_password(self):

        self.setting_frame.pack_forget()

        self.setting_password_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.setting_password_frame.pack(side="top", pady=150)

        self.setting_password_label1 = tk.Label(self.setting_password_frame, text=f"Old Password :--> ", font="times 20 bold")
        self.setting_password_label1.grid(row=1, column=0, padx=10, pady=10)

        self.setting_password_entry1 = tk.Entry(self.setting_password_frame, textvariable=self.old_password, show='*')
        self.setting_password_entry1.grid(row=1, column=1)

        self.setting_password_label2 = tk.Label(self.setting_password_frame, text=f"New Password :--> ",
                                                font="times 20 bold")
        self.setting_password_label2.grid(row=2, column=0, padx=10, pady=10)

        self.setting_password_entry2 = tk.Entry(self.setting_password_frame, textvariable=self.new_password, show='*')
        self.setting_password_entry2.grid(row=2, column=1)

        self.setting_password_label3 = tk.Label(self.setting_password_frame, text=f"Verify New Password :--> ",
                                                font="times 20 bold")
        self.setting_password_label3.grid(row=3, column=0, padx=10, pady=10)

        self.setting_password_entry3 = tk.Entry(self.setting_password_frame, textvariable=self.verify_new_password, show='*')
        self.setting_password_entry3.grid(row=3, column=1)

        self.setting_password_button5 = tk.Button(self.setting_password_frame, text='<<<--Back', fg='blue',
                                         command=self.setting_password_back,
                                         font="times 15 bold")
        self.setting_password_button5.grid(row=4, column=0, columnspan=2, pady=10)

        self.setting_password_button5 = tk.Button(self.setting_password_frame, text='*Update*', fg='blue',
                                                  command=self.setting_password_update,
                                                  font="times 15 bold")
        self.setting_password_button5.grid(row=4, column=2, columnspan=2, pady=10)


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx"""

    def setting_password_back(self):
        self.setting_password_frame.pack_forget()
        self.setting_label_detail.pack_forget()

        self.setting()



    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def setting_password_update(self):

        if self.password.get() == self.old_password.get():
            if self.new_password.get() == self.verify_new_password.get():
                cmd1 = f"update xyz set password='{self.new_password.get()}' where username='{self.username.get()}'"
                db_execute_fetch(cmd1)

                tmsg.showinfo('Setting', 'Message--->>> Your Password Is Updated Successfully.....')

                self.setting_password_frame.pack_forget()
                self.password.set('')
                self.old_password.set('')
                self.new_password.set('')
                self.verify_new_password.set('')

                self.setting_label_detail.pack_forget()
                self.image_delete()

                self.menu()

            else:
                tmsg.showwarning('Setting', 'Warning--->>> Password Verification is Failed..Please Enter Correct Password...')


        else:
            tmsg.showwarning('Setting', 'Warning-->>> Your Old Password Does Not Match...Please Enter Correct Password....')

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def setting_name(self):

        self.setting_frame.pack_forget()

        self.setting_name_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.setting_name_frame.pack(side="top", pady=150)

        self.setting_name_label1 = tk.Label(self.setting_name_frame, text=f"First Name :--> ",
                                                font="times 20 bold")
        self.setting_name_label1.grid(row=1, column=0, padx=10, pady=10)

        self.setting_name_entry1 = tk.Entry(self.setting_name_frame, textvariable=self.new_first_name)
        self.setting_name_entry1.grid(row=1, column=1)

        self.setting_name_label2 = tk.Label(self.setting_name_frame, text=f"Last Name :--> ",
                                            font="times 20 bold")
        self.setting_name_label2.grid(row=2, column=0, padx=10, pady=10)

        self.setting_name_entry2 = tk.Entry(self.setting_name_frame, textvariable=self.new_last_name)
        self.setting_name_entry2.grid(row=2, column=1)

        self.setting_name_button5 = tk.Button(self.setting_name_frame, text='<<<--Back', fg='blue',
                                                  command=self.setting_name_back,
                                                  font="times 15 bold")
        self.setting_name_button5.grid(row=3, column=0,  pady=10)

        self.setting_name_button5 = tk.Button(self.setting_name_frame, text='*Update*', fg='blue',
                                              command=self.setting_name_update,
                                              font="times 15 bold")
        self.setting_name_button5.grid(row=3, column=1, columnspan=2, pady=10)

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_name_back(self):
        self.setting_name_frame.pack_forget()
        self.setting_label_detail.pack_forget()

        self.setting()

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_name_update(self):

        cmd1 = f"update xyz set first_name='{self.new_first_name.get()}' where username='{self.username.get()}'"
        db_execute_fetch(cmd1)

        cmd2 = f"update xyz set last_name='{self.new_last_name.get()}' where username='{self.username.get()}'"
        db_execute_fetch(cmd2)



        tmsg.showinfo('Setting', f'Message--->>> Your Name Is Updated Successfully...Your New Name Is-->>  {self.new_first_name.get().title()} {self.new_last_name.get().title()}.....')

        self.setting_name_frame.pack_forget()

        self.new_first_name.set('')
        self.new_last_name.set('')

        self.setting_label_detail.pack_forget()

        self.setting()


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_email(self):

        self.setting_frame.pack_forget()

        self.setting_email_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.setting_email_frame.pack(side="top", pady=150)

        self.setting_email_label1 = tk.Label(self.setting_email_frame, text=f"Enter New Email :--> ",
                                            font="times 20 bold")
        self.setting_email_label1.grid(row=1, column=0, padx=10, pady=10)

        self.setting_email_entry1 = tk.Entry(self.setting_email_frame, textvariable=self.new_email)
        self.setting_email_entry1.grid(row=1, column=1)


        self.setting_email_button5 = tk.Button(self.setting_email_frame, text='<<<--Back', fg='blue',
                                              command=self.setting_email_back,
                                              font="times 15 bold")
        self.setting_email_button5.grid(row=3, column=0, pady=10)

        self.setting_email_button5 = tk.Button(self.setting_email_frame, text='*Update*', fg='blue',
                                              command=self.setting_email_update,
                                              font="times 15 bold")
        self.setting_email_button5.grid(row=3, column=1, columnspan=2, pady=10)

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_email_back(self):
        self.setting_email_frame.pack_forget()
        self.setting_label_detail.pack_forget()

        self.setting()

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_email_update(self):

        cmd1 = f"update xyz set email='{self.new_email.get()}' where username='{self.username.get()}'"
        db_execute_fetch(cmd1)


        tmsg.showinfo('Setting', f'Message--->>> Your Email Is Updated Successfully...Your New Email Is -> {self.new_email.get()}.......')

        self.setting_email_frame.pack_forget()

        self.new_email.set('')

        self.setting_label_detail.pack_forget()

        self.setting()


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def setting_phone_number(self):

        self.setting_frame.pack_forget()

        self.setting_phone_number_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.setting_phone_number_frame.pack(side="top", pady=150)

        self.setting_phone_number_label1 = tk.Label(self.setting_phone_number_frame, text=f"Enter New Phone Number :--> ",
                                             font="times 20 bold")
        self.setting_phone_number_label1.grid(row=1, column=0, padx=10, pady=10)

        self.setting_phone_number_entry1 = tk.Entry(self.setting_phone_number_frame, textvariable=self.new_phone_number)
        self.setting_phone_number_entry1.grid(row=1, column=1)

        self.setting_phone_number_button5 = tk.Button(self.setting_phone_number_frame, text='<<<--Back', fg='blue',
                                               command=self.setting_phone_number_back,
                                               font="times 15 bold")
        self.setting_phone_number_button5.grid(row=3, column=0, pady=10)

        self.setting_phone_number_button5 = tk.Button(self.setting_phone_number_frame, text='*Update*', fg='blue',
                                               command=self.setting_phone_number_update,
                                               font="times 15 bold")
        self.setting_phone_number_button5.grid(row=3, column=1, columnspan=2, pady=10)

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_phone_number_back(self):
        self.setting_phone_number_frame.pack_forget()
        self.setting_label_detail.pack_forget()

        self.setting()

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def setting_phone_number_update(self):


        if len(self.new_phone_number.get()) == 10:
            try:

                new_ph = int(self.new_phone_number.get())
                cmd1 = f"update xyz set phone_number='{new_ph}' where username='{self.username.get()}'"
                db_execute_fetch(cmd1)

                tmsg.showinfo('Setting',
                              f'Message--->>> Your phone_number Is Updated Successfully...Your New phone_number Is -> {new_ph}.......')

                self.setting_phone_number_frame.pack_forget()
                self.setting_label_detail.pack_forget()

                self.new_phone_number.set('')

                self.setting()

            except Exception as e:
                tmsg.showwarning('Setting', 'Warning--->>>  Enter Only Numerical Digits......')

        else:
            tmsg.showwarning('Setting', 'Warning--->>> Enter Only 10 Digits Phone Number.....')


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""


    def setting_back(self):
        self.setting_frame.pack_forget()
        self.setting_label_detail.pack_forget()

        self.login()


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



    def signup(self):

        self.menu_frame.pack_forget()

        self.signup_frame = tk.Frame(self.root, bg='#FAF0E6', relief='sunken', borderwidth=9)
        self.signup_frame.pack(side="top", pady=50)

        self.signup_label1 = tk.Label(self.signup_frame, text="***Enter Your Details To Signup ***", bg='#FFA07A', font="times 35 bold")
        self.signup_label1.grid(row=0, column=0, padx=10, columnspan=3)

        ask_list = ['Username', 'First Name', 'Last Name', 'Password', 'Verify Password', 'Email', 'Phone Number']
        for i in range(0, len(ask_list)):
            self.signup_label2 = tk.Label(self.signup_frame, text=f"{ask_list[i]}:--> ", font="times 20 bold")
            self.signup_label2.grid(row=i+1, column=1, padx=10, pady=10)


        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.username)
        self.signup_entry1.grid(row=1, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.first_name)
        self.signup_entry1.grid(row=2, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.last_name)
        self.signup_entry1.grid(row=3, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.password, show='*')
        self.signup_entry1.grid(row=4, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.verify_password, show='*')
        self.signup_entry1.grid(row=5, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.email)
        self.signup_entry1.grid(row=6, column=2)

        self.signup_entry1 = tk.Entry(self.signup_frame, textvariable=self.phone_number)
        self.signup_entry1.grid(row=7, column=2)

        self.signup_button1 = tk.Button(self.signup_frame, text='*Login*', fg='blue', command=self.signup_login,
                                      font="times 15 bold")
        self.signup_button1.grid(row=9, column=1, pady=20, padx=10,columnspan=3)

        self.signup_button2 = tk.Button(self.signup_frame, text='*Signup*', fg='blue', command=self.signup_submit,
                                      font="times 15 bold")
        self.signup_button2.grid(row=9, column=2, pady=20)



        """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def signup_login(self):
        self.signup_frame.pack_forget()
        self.menu_label.pack_forget()

        self.image_delete()

        self.menu()

    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def signup_submit(self):

        try:

            cmd = f"select * from xyz where username='{self.username.get()}'"
            db_connection()
            db_execute_fetch(cmd)

            if not data:
                if self.password.get() == self.verify_password.get():

                    while True:
                        q, w, e, r, t, y, u, i, o, p, l = map(str, [randint(0, 9) for i in range(11)])
                        """Assigning 11 random number to update
                        account-number in database."""
                        a = q + w + e + r + t + y + u + i + o + p + l

                        cmd1 = "select * from xyz where account_number='{a}'"
                        # Here I am not database' functions which I created above.
                        cursor.execute(cmd1)
                        data1 = cursor.fetchall()
                        if data1:
                            """checking whether a randomly generated account number is already
                            in bank databse or not."""
                            continue
                        else:
                            break



                    if len(self.phone_number.get()) == 10:
                        try:

                            int_phone_number = int(self.phone_number.get())
                            cmd2 = f"insert into xyz values('{self.username.get()}','{self.first_name.get()}','{self.last_name.get()}',0,'{a}','{self.password.get()}','{self.email.get()}','{int_phone_number}')"
                            db_execute_insert(cmd2)
                            db_close()

                            tmsg.showinfo('Signup', f'Hello {self.first_name.get().title()} {self.last_name.get().title()}...Account Is Successfully Created With Initial Balance Of  Rs 0  ...Your Account Number is -->> {a}.......... Enjoy The Services Of XYZ Bank....Have A Nice Day...')


                            self.username.set('')
                            self.phone_number.set('')
                            self.first_name.set('')
                            self.last_name.set('')
                            self.password.set('')
                            self.verify_password.set('')
                            self.email.set('')


                            self.signup_login()

                        except Exception as e:
                            tmsg.showwarning('Signup', 'Warning-->>>  Enter Only Digits.....')

                    else:
                        tmsg.showwarning('Signup', 'Warning--->>>  Enter Only 10 Digits Phone Number..... ')

                else:
                    tmsg.showwarning("Signup", "Warning-->>>>  Password Verification is Failed....Please Verify Your Password Again")

            else:
                tmsg.showinfo("Signup", "Sorry---->>>>>   Username has been Already Taken...Please Choose Another Username..")



        except Exception as e:
            tmsg.showerror('Error', f'Error-->>>  {e}')


    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""



"""***********************************************************************************************************************"""


if __name__=="__main__":
    window = Bank()
    window.menu()
    window.root.mainloop()



