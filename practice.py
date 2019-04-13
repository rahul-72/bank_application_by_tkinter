import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

image = Image.open("static/images/1.jpg")
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()


root.mainloop()