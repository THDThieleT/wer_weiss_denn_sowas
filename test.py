import tkinter as tk
from PIL import Image, ImageTk
 
class Window:
    def __init__(self, master):
        self.img = Image.open("mushroom.png")
        self.img = self.img.resize((320, 300), Image.ANTIALIAS)
 
        self.img = ImageTk.PhotoImage(self.img)
 
        label = tk.Label(master, image = self.img)
        label.pack(expand = True, fill = tk.BOTH)
 
win = tk.Tk()
root = tk.Tk()
window = Window(root)
win.mainloop()