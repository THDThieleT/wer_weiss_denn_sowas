# Import the required Libraries
from tkinter import *
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
from pygame import mixer
from PIL import Image, ImageTk
import json

#TO DO: Themen Buttons grau werden lassen und Farbe ändern; Button Grafiken, auflösungsfilme????

class Quiz:
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.title("Wer weiß denn sowas???")
        self.main_screen.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Set the geometry of Tkinter frame
        self.main_screen.geometry("1920x1080")
        self.main_screen.state("zoomed")
        #self.main_screen.configure(bg=("dark grey"))
        self.buttons = [Button] * 12
        self.answer_buttons = [Button] * 3
        self.active_button = -1
        self.question_index = -1
        self.answered = True
        self.correct = False
        file = open("daten.json", encoding="UTF-8")
        self.data = json.load(file)
        
        self.window = Toplevel
        self.answer_window = Toplevel

        self.rahmen = ImageTk.PhotoImage(Image.open("Bilder/rahmen.png"))
        self.korrekt = ImageTk.PhotoImage(Image.open("Bilder/korrekt.png"))
        self.falsch = ImageTk.PhotoImage(Image.open("Bilder/falsch.png"))    
        self.grau = ImageTk.PhotoImage(Image.open("Bilder/grau.png"))
        self.antwort_rahmen = ImageTk.PhotoImage(Image.open("Bilder/antwort_rahmen.png"))
        self.antwort_korrekt = ImageTk.PhotoImage(Image.open("Bilder/antwort_richtig.png"))
        self.antwort_falsch = ImageTk.PhotoImage(Image.open("Bilder/antwort_falsch.png"))
        self.antwort_select = ImageTk.PhotoImage(Image.open("Bilder/antwort_select.png"))
        
        temp_index = 0
        for i in range(0, 3):
            for j in range(0, 4):
                button = Button(
                    self.main_screen,
                    text=self.data["themen"][temp_index],
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    width= 480,
                    height= 360,
                    image=self.rahmen,
                    compound=CENTER,
                )
                button.grid(column=j, row=i)
                self.buttons[temp_index] = button
                temp_index += 1
        temp = self.buttons[0]
        temp.configure(command=lambda: self.load_question(0))
        temp = self.buttons[1]
        temp.configure(command=lambda: self.load_question(1))
        temp = self.buttons[2]
        temp.configure(command=lambda: self.load_question(2))
        temp = self.buttons[3]
        temp.configure(command=lambda: self.load_question(3))
        temp = self.buttons[4]
        temp.configure(command=lambda: self.load_question(4))
        temp = self.buttons[5]
        temp.configure(command=lambda: self.load_question(5))
        temp = self.buttons[6]
        temp.configure(command=lambda: self.load_question(6))
        temp = self.buttons[7]
        temp.configure(command=lambda: self.load_question(7))
        temp = self.buttons[8]
        temp.configure(command=lambda: self.load_question(8))
        temp = self.buttons[9]
        temp.configure(command=lambda: self.load_question(9))
        temp = self.buttons[10]
        temp.configure(command=lambda: self.load_question(10))
        temp = self.buttons[11]
        temp.configure(command=lambda: self.load_question(11))
        self.main_screen.mainloop()

    def set_index(self, index):
        self.question_index = index

    def set_main_button(self, color):
        if (color == self.grau):
            temp = self.buttons[self.question_index]
            temp.configure(image= self.grau)
        else:
            temp = self.buttons[self.question_index]
            temp.configure(image= color, command=lambda:None)

    def pressed_button_a(self):
        if self.answered == False:
            if not (self.active_button == 0):
                temp = self.answer_buttons[self.active_button]
                temp.configure(image= self.antwort_rahmen)
                temp = self.answer_buttons[0]
                temp.configure(image= self.antwort_select)
                self.active_button = 0
            else:
                self.answered = True
                if self.data["fragen"][self.question_index]["correct"] == 1:
                    temp = self.answer_buttons[0]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.korrekt)
                    self.correct = True
                else:
                    temp = self.answer_buttons[0]
                    temp.configure(image= self.antwort_falsch)
                    temp = self.answer_buttons[self.data["fragen"][self.question_index]["correct"] - 1]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.falsch)
                    self.correct = False
                
                for i in range(0,3):
                    temp = self.answer_buttons[i]
                    temp.configure(command=lambda:None)
                self.play_answer()
        
    def pressed_button_b(self):
        if self.answered == False:
            if not (self.active_button == 1):
                temp = self.answer_buttons[self.active_button]
                temp.configure(image= self.antwort_rahmen)
                temp = self.answer_buttons[1]
                temp.configure(image= self.antwort_select)
                self.active_button = 1
            else:
                self.answered = True
                if self.data["fragen"][self.question_index]["correct"] == 2:
                    temp = self.answer_buttons[1]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.korrekt)
                    self.correct = True
                else:
                    temp = self.answer_buttons[1]
                    temp.configure(image= self.antwort_falsch)
                    temp = self.answer_buttons[self.data["fragen"][self.question_index]["correct"] - 1]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.falsch)
                    self.correct = False

                for i in range(0,3):
                    temp = self.answer_buttons[i]
                    temp.configure(command=lambda:None)
                self.play_answer()

    def pressed_button_c(self):
        if self.answered == False:
            if not (self.active_button == 2):
                temp = self.answer_buttons[self.active_button]
                temp.configure(image= self.antwort_rahmen)
                temp = self.answer_buttons[2]
                temp.configure(image= self.antwort_select)
                self.active_button = 2
            else:
                self.answered = True
                if self.data["fragen"][self.question_index]["correct"] == 3:
                    temp = self.answer_buttons[2]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.korrekt)
                    self.correct = True
                else:
                    temp = self.answer_buttons[2]
                    temp.configure(image= self.antwort_falsch)
                    temp = self.answer_buttons[self.data["fragen"][self.question_index]["correct"] - 1]
                    temp.configure(image= self.antwort_korrekt)
                    self.set_main_button(self.falsch)
                    self.correct = False
                
                for i in range(0,3):
                    temp = self.answer_buttons[i]
                    temp.configure(command=lambda:None)
                self.play_answer()

    def load_question(self, question_number):
        self.active_button = -1
        self.answered = False
        self.set_index(self.data["fragen"][question_number]["index"])
        self.set_main_button(self.grau)
        self.window = Toplevel(width=1920, height=1080, bg="white")
        self.window.state("zoomed")
        img = Image.open(self.data["fragen"][question_number]["pic"])
        img = img.crop((0, 100, 1920, 750))
        img = ImageTk.PhotoImage(img)
        temp_label = Label(self.window, borderwidth=0, image=img)
        temp_label.grid(column=0, row=0)
        temp_label = Label(self.window, text=self.data["fragen"][question_number]["frage"] , font=("Arial", 25, "bold"), pady=10, bg="white", borderwidth=0)
        temp_label.grid(column=0, row=1)  
        button = Button(
                self.window,
                text=self.data["fragen"][question_number]["answer1"],
                height=84,
                width=1588,
                font=("Arial", 20, "bold"),
                fg="white", bg="white",
                image= self.antwort_rahmen,
                pady=5,
                borderwidth=0,
                compound=CENTER,
                command=self.pressed_button_a,
            )
        button.grid(column=0, row=2)
        self.answer_buttons[0] = button
        
        button = Button(
                self.window,
                text=self.data["fragen"][question_number]["answer2"],
                height=84,
                width=1588,
                font=("Arial", 20, "bold"),
                fg="white", bg="white",
                image= self.antwort_rahmen,
                pady=5,            
                borderwidth=0,
                compound=CENTER,
                command=self.pressed_button_b,
            )
        button.grid(column=0, row=3)
        self.answer_buttons[1] = button
        
        button = Button(
                self.window,
                text=self.data["fragen"][question_number]["answer3"],
                height=84,
                width=1588,
                font=("Arial", 20, "bold"),
                fg="white", bg="white",
                image= self.antwort_rahmen,
                pady=5,
                borderwidth=0,
                compound=CENTER,
                command=self.pressed_button_c,
            )
        button.grid(column=0, row=4)
        self.answer_buttons[2] = button
        self.window.mainloop()

    def end_video(self, event):
        #mixer.init()
        if(self.correct):
            mixer.music.load("Videos/richtig.mp3")
        else:
            mixer.music.load("Videos/wrong.mp3")
        mixer.music.play()
        self.answer_window.destroy()

    def play_answer(self):
        mixer.init()
        self.answer_window = Toplevel(width=1920, height=1080, bg="white")
        self.answer_window.state("zoomed")
        videoplayer = TkinterVideo(master=self.answer_window, scaled=True) 
        videoplayer.load(self.data["fragen"][self.question_index]["video"])
        videoplayer.pack(expand=True, fill="both")
        mixer.music.load(self.data["fragen"][self.question_index]["audio"])
        videoplayer.play() # play the video
        mixer.music.play()
        videoplayer.bind("<<Ended>>", self.end_video)

    def on_closing(self):
        if messagebox.askokcancel("Beenden", "Möchtest du das Quiz wirklich beenden und den Fortschritt löschen?"):
            self.main_screen.destroy()

if __name__ == "__main__":
    quiz = Quiz()
