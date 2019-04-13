import tkinter as tk

root = tk.Tk()
b = tk.StringVar()

def hello():
    try:
        q = int(b.get())
        print(q)
        print(type(q))

    except ValueError:
        print("hi")

a = tk.Entry(root, textvariable=b).pack()
bu= tk.Button(root, text='submit', command=hello).pack()


root.mainloop()