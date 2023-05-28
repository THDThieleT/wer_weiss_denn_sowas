#Import the required Libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Window:
    def __init__(self, master):
        self.img = Image.open("mushroom.png")
        self.img = self.img.resize((320, 300), Image.ANTIALIAS)
 
        self.img = ImageTk.PhotoImage(self.img)
 
        label = Label(master, image = self.img)
        label.pack(expand = True, fill = BOTH)

def press_button1():
    #overwrite Button    
    global button_1
    button_1 = Button(win, text= "Thema 1", default="disabled", height=5, width=20, font=("Arial",20,"bold"),bg="grey", command= None).grid(column=0, row=0)
    #Create new Window for question
    question= Toplevel()
    question.geometry("1920x1080")
    img = Image.open("mushroom.png")
    img = ImageTk.PhotoImage(img)
    picture = Label(question, image= img)
    picture.place(relx=0, rely=0)
    question.mainloop()






#Create an instance of Tkinter frame
win= Tk()
win.title("Wer weiß denn sowas???")
#Set the geometry of Tkinter frame
win.geometry("1920x1080")
win.configure(bg=("dark grey"))


button_1 = Button(win, text= "Thema 1", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= press_button1).grid(column=0, row=0)
button_2 = Button(win, text= "Thema 2", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=1, row=0)
button_3 = Button(win, text= "Thema 3", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=2, row=0)
button_4 = Button(win, text= "Thema 4", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=3, row=0)
button_5 = Button(win, text= "Thema 5", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=0, row=1)
button_6 = Button(win, text= "Thema 6", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=1, row=1)
button_7 = Button(win, text= "Thema 7", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=2, row=1)
button_8 = Button(win, text= "Thema 8", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=3, row=1)
button_9 = Button(win, text= "Thema 9", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=0, row=2)
button_10 = Button(win, text= "Thema 10", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=1, row=2)
button_11 = Button(win, text= "Thema 11", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=2, row=2)
button_12 = Button(win, text= "Thema 12", height=5, width=20, font=("Arial",20,"bold"),bg="light blue", command= None).grid(column=3, row=2)
win.mainloop()


