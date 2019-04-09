import tkinter as tk

root=tk.Tk()

#we can create only one root object.
"""we have to create a Tk root widget, which is a window with a title bar and 
other decoration provided by the window manager. 
The root widget has to be created before any other widgets and 
there can only be one root widget."""

w=tk.Label(root, text="Hello tkinter")

"""The next line of code contains the Label widget. 
The first parameter of the Label call is the name of the parent window, 
in our case "root". So our Label widget is a child of the root widget. 
The keyword parameter "text" specifies the text to be shown:"""

w.pack()

root.mainloop()