import tkinter as tk

root = tk.Tk()
b = tk.IntVar()
def hello():
    #print(a.get())
    try:
        if b.get()!="":
            print(int(b.get()))
        else:
            print("Enter amount")
    except Exception as e:
        print(e)
a = tk.Entry(root, textvariable=b).pack()
bu= tk.Button(root, text='submit', command=hello).pack()


root.mainloop()