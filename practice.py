import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
q = tk.StringVar()

def hello():
    print(q.get())
    if q.get():
        print('hi')

    else:
        print('hello')
entry = tk.Entry(root, textvariable=q).pack()
button = tk.Button(root, text='submit', command=hello).pack()


root.mainloop()