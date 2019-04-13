import tkinter as tk

root = tk.Tk()
b = tk.StringVar()
w=5
def hello():
    try:
        q = int(b.get())
        print(q)
        try:
            w+=1
        except Exception as e:
            print(e)

        print(type(q))

    except ValueError:
        print("hi")

a = tk.Entry(root, textvariable=b).pack()
bu= tk.Button(root, text='submit', command=hello).pack()


root.mainloop()