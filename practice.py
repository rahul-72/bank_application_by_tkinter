import tkinter as tk

root = tk.Tk()
b = tk.StringVar()
def hello():
    try:
        print(int(b.get()))

    except ValueError:
        print("hi")

a = tk.Entry(root, textvariable=b).pack()
bu= tk.Button(root, text='submit', command=hello).pack()


root.mainloop()