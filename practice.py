import tkinter as tk

root = tk.Tk()


class A:
    def __init__(self):
        self.username = tk.StringVar()



    def hi(self):
        userentry = tk.Entry(root, textvariable=self.username).pack()
        button1 = tk.Button(root, text='submit', command=self.hello).pack()
    def hello(self):
        print(self.username.get())
a=A()
a.hi()


root.mainloop()