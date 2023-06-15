# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import json

#TO DO: Themen Buttons grau werden lassen und Farbe ändern; Button Grafiken, auflösungsfilme????

themen = '{"thema1":"Clever", "thema2":"Total Genial", "thema3":"Gesundheit", "thema4":"tierisch, tierisch", "thema5":"Trick 17", "thema6":"Auto", "thema7":"?", "thema8":"Im Grünen", "thema9":"Vereine", "thema10":"Heimat", "thema11":"Sport", "thema12":"Brisant!"  }'
frage1 = '{ "pic":"Bilder/frage1.png", "answer1":"Columbo", "answer2":"Monk", "answer3":"Johannes Staller", "correct":1, "index":0}'
frage2 = '{ "pic":"Bilder/frage2.png", "answer1":"Leidenschaft unter dem See Tanz", "answer2":"Verliebt unter dem See Tanz", "answer3":"Verzauberung unter dem See Tanz", "correct":3, "index":1}'
frage3 = '{ "pic":"Bilder/frage3.png", "answer1":"22 Oktober 1984 - 25. März 1988", "answer2":"22 Oktober 1985 - 25. März 1989", "answer3":"22 Oktober 1986 - 25. März 1990", "correct":2, "index":2}'
frage4 = '{ "pic":"Bilder/frage4.png", "answer1":"Grün-Blau", "answer2":"Grün-Gelb", "answer3":"Orange-Gelb", "correct":3, "index":3}'
frage5 = '{ "pic":"Bilder/frage5.png", "answer1":"Kaugummi", "answer2":"Schokolade", "answer3":"Kartoffel", "correct":2, "index":4}'
frage6 = '{ "pic":"Bilder/frage6.png", "answer1":"K.I.T.T und der Delorean wurden von der selben Person designed", "answer2":"Musik ist vom selben Komponisten", "answer3":"Beides kam im selben Jahr heraus", "correct":1, "index":5}'
frage7 = '{ "pic":"Bilder/frage7.png", "answer1":"Die Miami Cops (1985)", "answer2":"Die Troublemaker (1994)", "answer3":"Vier Fäuste gegen Rio", "correct":2, "index":6}'
frage8 = '{ "pic":"Bilder/frage8.png", "answer1":"100 - 119", "answer2":"Keine", "answer3":"60-80", "correct":1, "index":7}'
frage9 = '{ "pic":"Bilder/frage9.png", "answer1":"Noah Weißhaupt", "answer2":"Matthias Ginter", "answer3":"Ritsu Doan", "correct":3, "index":8}'
frage10 = '{ "pic":"Bilder/frage10.png", "answer1":"Pfeil", "answer2":"Edelweiß", "answer3":"Libelle", "correct":1, "index":9}'
frage11 = '{ "pic":"Bilder/frage11.png", "answer1":"1945er Ford Cabrio", "answer2":"1947er Ford Cabrio", "answer3":"1950er Ford Cabrio", "correct":2, "index":10}'
frage12 = '{ "pic":"Bilder/frage12.png", "answer1":"540", "answer2":"560", "answer3":"580", "correct":1, "index":11}'

class Quiz:
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.title("Wer weiß denn sowas???")
        self.main_screen.protocol("WM_DELETE_WINDOW", DISABLED)

        # Set the geometry of Tkinter frame
        self.main_screen.geometry("1920x1080")
        self.main_screen.state("zoomed")
        #self.main_screen.configure(bg=("dark grey"))
        self.buttons = [Button] * 12
        self.active_button = 0
        self.answered = True
        self.data = json.loads(themen)

        self.rahmen = ImageTk.PhotoImage(Image.open("Bilder/rahmen.png"))
        self.korrekt = ImageTk.PhotoImage(Image.open("Bilder/korrekt.png"))
        self.falsch = ImageTk.PhotoImage(Image.open("Bilder/falsch.png"))    
        self.grau = ImageTk.PhotoImage(Image.open("Bilder/grau.png"))
        self.antwort_rahmen = ImageTk.PhotoImage(Image.open("Bilder/antwort_rahmen.png"))
        self.antwort_korrekt = ImageTk.PhotoImage(Image.open("Bilder/antwort_richtig.png"))
        self.antwort_falsch = ImageTk.PhotoImage(Image.open("Bilder/antwort_falsch.png"))
        self.antwort_select = ImageTk.PhotoImage(Image.open("Bilder/antwort_select.png"))
        
        self.button1 = Button(
            self.main_screen,
            text=self.data["thema1"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage1),
        )
        self.button1.grid(column=0, row=0)
        self.button2 = Button(
            self.main_screen,
            text=self.data["thema2"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage2),
        )
        self.button2.grid(column=1, row=0)
        self.button3 = Button(
            self.main_screen,
            text=self.data["thema3"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage3),
        )
        self.button3.grid(column=2, row=0)
        self.button4 = Button(
            self.main_screen,
            text=self.data["thema4"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage4),
        )
        self.button4.grid(column=3, row=0)
        self.button5 = Button(
            self.main_screen,
            text=self.data["thema5"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage5),
        )
        self.button5.grid(column=0, row=1)
        self.button6 = Button(
            self.main_screen,
            text=self.data["thema6"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage6),
        )
        self.button6.grid(column=1, row=1)
        self.button7 = Button(
            self.main_screen,
            text=self.data["thema7"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage7),
        )
        self.button7.grid(column=2, row=1)
        self.button8 = Button(
            self.main_screen,
            text=self.data["thema8"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage8),
        )
        self.button8.grid(column=3, row=1)
        self.button9 = Button(
            self.main_screen,
            text=self.data["thema9"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage9),
        )
        self.button9.grid(column=0, row=2)
        self.button10 = Button(
            self.main_screen,
            text=self.data["thema10"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage10),
        )
        self.button10.grid(column=1, row=2)
        self.button11 = Button(
            self.main_screen,
            text=self.data["thema11"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage11),
        )
        self.button11.grid(column=2, row=2)
        self.button12 = Button(
            self.main_screen,
            text=self.data["thema12"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            width= 480,
            height= 360,
            image=self.rahmen,
            compound=CENTER,
            command=lambda: self.load_question(frage12),
        )
        self.button12.grid(column=3, row=2)

        self.answer_button_a = Button()
        self.answer_button_b = Button()
        self.answer_button_c = Button()
        self.window = Toplevel
        self.main_screen.mainloop()

    def set_main_button(self, color):
        index = self.data["index"]
        temp = json.loads(themen)
        if(index == 0):
            self.button1.configure(
            text=temp["thema1"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        
        elif(index == 1):
            self.button2.configure(
            text=temp["thema2"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )

        elif(index == 2):
            self.button3.configure(
            text=temp["thema3"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        elif(index == 3):
            self.button4.configure(
            text=temp["thema4"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        elif(index == 4):
            self.button5.configure(
            text=temp["thema5"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
        
        elif(index == 5):
            self.button6.configure(
            text=temp["thema5"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )

        elif(index == 6):
            self.button7.configure(
            text=temp["thema7"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        elif(index == 7):
            self.button8.configure(
            text=temp["thema8"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        elif(index == 8):
            self.button9.configure(
            text=temp["thema9"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
        
        elif(index == 9):
            self.button10.configure(
            text=temp["thema10"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )

        elif(index == 10):
            self.button11.configure(
            text=temp["thema11"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )
            
        elif(index == 11):
            self.button12.configure(
            text=temp["thema12"],
            font=("Arial", 20, "bold"),
            fg="white", bg="white",
            image=color,
            compound=CENTER,
            command=None
            )

    def pressed_button_a(self):
        if self.answered == False:
            if not (self.active_button == 1):
                self.active_button = 1
                self.answer_button_a.configure(
                    text=self.data["answer1"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_select,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_a
                    )
                self.answer_button_b.configure(
                    text=self.data["answer2"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_rahmen,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_b
                    )
                self.answer_button_c.configure(
                    text=self.data["answer3"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_rahmen,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_c
                    )

            elif not self.answered:
                self.answered = True
                if self.data["correct"] == 1:
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.set_main_button(self.korrekt)
                else:
                    self.set_main_button(self.falsch)
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_falsch,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                if self.data["correct"] == 2:
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                elif self.data["correct"] == 3:
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
        
    def pressed_button_b(self):
        if self.answered == False:
            if not (self.active_button == 2):
                self.active_button = 2
                self.answer_button_a.configure(
                text=self.data["answer1"],
                height=84,
                width=1588,
                font=("Arial", 20, "bold"),
                fg="white", bg="white",
                image= self.antwort_rahmen,
                pady=5,
                borderwidth=0,
                compound=CENTER,
                command=self.pressed_button_a
                )
                self.answer_button_b.configure(
                    text=self.data["answer2"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_select,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_b
                    )
                self.answer_button_c.configure(
                    text=self.data["answer3"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_rahmen,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_c
                    )

            elif not self.answered:
                self.answered = True
                if self.data["correct"] == 2:
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.set_main_button(self.korrekt)
                else:
                    self.set_main_button(self.falsch)
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_falsch,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                if self.data["correct"] == 1:
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                elif self.data["correct"] == 3:
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )

    def pressed_button_c(self):
        if self.answered == False:
            if not (self.active_button == 3):
                self.active_button = 3
                self.answer_button_a.configure(
                text=self.data["answer1"],
                height=84,
                width=1588,
                font=("Arial", 20, "bold"),
                fg="white", bg="white",
                image= self.antwort_rahmen,
                pady=5,
                borderwidth=0,
                compound=CENTER,
                command=self.pressed_button_a
                )
                self.answer_button_b.configure(
                    text=self.data["answer2"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_rahmen,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_b
                    )
                self.answer_button_c.configure(
                    text=self.data["answer3"],
                    height=84,
                    width=1588,
                    font=("Arial", 20, "bold"),
                    fg="white", bg="white",
                    image= self.antwort_select,
                    pady=5,
                    borderwidth=0,
                    compound=CENTER,
                    command=self.pressed_button_c
                    )
            elif not self.answered:
                self.answered = True
                if self.data["correct"] == 3:
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.set_main_button(self.korrekt)
                else:
                    self.set_main_button(self.falsch)
                    self.answer_button_c.configure(
                        text=self.data["answer3"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_falsch,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                if self.data["correct"] == 1:
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                elif self.data["correct"] == 2:
                    self.answer_button_a.configure(
                        text=self.data["answer1"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_rahmen,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )
                    self.answer_button_b.configure(
                        text=self.data["answer2"],
                        height=84,
                        width=1588,
                        font=("Arial", 20, "bold"),
                        fg="white", bg="white",
                        image= self.antwort_korrekt,
                        pady=5,
                        borderwidth=0,
                        compound=CENTER,
                        command=None
                        )

    def load_question(self, question_number):
        if self.answered == True:
            self.active_button = 0
            self.answered = False
            self.data = json.loads(question_number)
            self.set_main_button(self.rahmen)
            self.window = Toplevel(width=1920, height=1080, bg="white")
            self.window.state("zoomed")
            img = Image.open(self.data["pic"])
            img = ImageTk.PhotoImage(img)
            Label(self.window, image=img).grid(column=0, row=0)
            print("Knopf A", self.answer_button_a)
            self.answer_button_a = Button(
                self.window,
                text=self.data["answer1"],
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
            self.answer_button_a.grid(column=0, row=1)
            print("Knopf B", self.answer_button_b)
            self.answer_button_b = Button(
                self.window,
                text=self.data["answer2"],
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
            self.answer_button_b.grid(column=0, row=2)
            print("Knopf C", self.answer_button_c)
            self.answer_button_c = Button(
                self.window,
                text=self.data["answer3"],
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
            self.answer_button_c.grid(column=0, row=3)
            self.window.mainloop()


if __name__ == "__main__":
    quiz = Quiz()
