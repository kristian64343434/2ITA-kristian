from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

photo = PhotoImage(file = r"https://cdn2.iconfinder.com/data/icons/flat-ui-icons-24-px/24/eye-24-256.png")
photoimage = photo.subsample(3, 3)
Button(root, text = 'Click Me !', image = photoimage,
                    compound = LEFT).pack(side = TOP)

root.mainloop()