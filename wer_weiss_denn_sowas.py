# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import json

#TO DO: Themen Buttons grau werden lassen und Farbe ändern; Button Grafiken, auflösungsfilme????

themen = '{"thema1":"Thema1", "thema2":"Thema2", "thema3":"Thema3", "thema4":"Thema4", "thema5":"Thema5", "thema6":"Thema6", "thema7":"Thema7", "thema8":"Thema8", "thema9":"Thema9", "thema10":"Thema10", "thema11":"Thema11", "thema12":"Thema12"  }'
frage1 = '{ "pic":"Bilder/aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":0}'
frage2 = '{ "pic":"Bilder/aal.png", "answer1":"neue Antwort1", "answer2":"Baum", "answer3":"elefant", "correct":2, "index":1}'
frage3 = '{ "pic":"Bilder/aal.png", "answer1":"12", "answer2":"18", "answer3":"45", "correct":1, "index":2}'
frage4 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":3}'
frage5 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":4}'
frage6 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":5}'
frage7 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":6}'
frage8 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":7}'
frage9 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":8}'
frage10 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":9}'
frage11 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":10}'
frage12 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3, "index":11}'


class Quiz:
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.title("Wer weiß denn sowas???")
        # Set the geometry of Tkinter frame
        self.main_screen.geometry("1920x1080")
        self.main_screen.configure(bg=("dark grey"))
        self.buttons = [Button] * 12
        self.active_button = 0
        self.answered = False
        self.data = json.loads(themen)

        self.button1 = Button(
            self.main_screen,
            text=self.data["thema1"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage1),
        ).grid(column=0, row=0)
        self.button2 = Button(
            self.main_screen,
            text=self.data["thema2"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage2),
        ).grid(column=1, row=0)
        self.button3 = Button(
            self.main_screen,
            text=self.data["thema3"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage3),
        ).grid(column=2, row=0)
        self.button4 = Button(
            self.main_screen,
            text=self.data["thema4"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage4),
        ).grid(column=3, row=0)
        self.button5 = Button(
            self.main_screen,
            text=self.data["thema5"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage5),
        ).grid(column=0, row=1)
        self.button6 = Button(
            self.main_screen,
            text=self.data["thema6"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage6),
        ).grid(column=1, row=1)
        self.button7 = Button(
            self.main_screen,
            text=self.data["thema7"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage7),
        ).grid(column=2, row=1)
        self.button8 = Button(
            self.main_screen,
            text=self.data["thema8"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage8),
        ).grid(column=3, row=1)
        self.button9 = Button(
            self.main_screen,
            text=self.data["thema9"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage9),
        ).grid(column=0, row=2)
        self.button10 = Button(
            self.main_screen,
            text=self.data["thema10"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage10),
        ).grid(column=1, row=2)
        self.button11 = Button(
            self.main_screen,
            text=self.data["thema11"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage11),
        ).grid(column=2, row=2)
        self.buttons12 = Button(
            self.main_screen,
            text=self.data["thema12"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage12),
        ).grid(column=3, row=2)

        self.answer_button_a = Button()
        self.answer_button_b = Button()
        self.answer_button_c = Button()
        self.window = Toplevel
        self.main_screen.mainloop()

    def set_main_button(self, color):
        index = self.data["index"]
        temp = json.loads(themen)
        if(index == 0):
            self.button1 = Button(
            self.main_screen,
            text=temp["thema1"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=0, row=0)
        
        elif(index == 1):
            self.button2 = Button(
            self.main_screen,
            text=temp["thema2"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=1, row=0)

        elif(index == 2):
            self.button3 = Button(
            self.main_screen,
            text=temp["thema3"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=2, row=0)
            
        elif(index == 3):
            self.button4 = Button(
            self.main_screen,
            text=temp["thema4"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=3, row=0)
            
        elif(index == 4):
            self.button5 = Button(
            self.main_screen,
            text=temp["thema5"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=0, row=1)
        
        elif(index == 5):
            self.button6 = Button(
            self.main_screen,
            text=temp["thema5"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=1, row=1)

        elif(index == 6):
            self.button7 = Button(
            self.main_screen,
            text=temp["thema7"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=2, row=1)
            
        elif(index == 7):
            self.button8 = Button(
            self.main_screen,
            text=temp["thema8"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=3, row=1)
            
        elif(index == 8):
            self.button9 = Button(
            self.main_screen,
            text=temp["thema9"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=0, row=2)
        
        elif(index == 9):
            self.button10 = Button(
            self.main_screen,
            text=temp["thema10"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=1, row=2)

        elif(index == 10):
            self.button7 = Button(
            self.main_screen,
            text=temp["thema11"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=2, row=2)
            
        elif(index == 11):
            self.button8 = Button(
            self.main_screen,
            text=temp["thema12"],
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg=color,
            command=None,
        ).grid(column=3, row=2)

    def pressed_button_a(self):
        if not (self.active_button == 1):
            self.active_button = 1
            self.answer_button_a = Button(
                self.window,
                text=self.data["answer1"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="yellow",
                pady=20,
                command=self.pressed_button_a,
            ).grid(column=0, row=1)
            self.answer_button_b = Button(
                self.window,
                text=self.data["answer2"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_b,
            ).grid(column=0, row=2)
            self.answer_button_c = Button(
                self.window,
                text=self.data["answer3"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_c,
            ).grid(column=0, row=3)

        elif not self.answered:
            self.answered = True
            if self.data["correct"] == 1:
                self.answer_button_a = Button(
                    self.window,
                    text=self.data["answer1"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="green",
                    pady=20,
                    command=None,
                ).grid(column=0, row=1)
                self.set_main_button("green")
            else:
                self.set_main_button("red")
                self.answer_button_a = Button(
                    self.window,
                    text=self.data["answer1"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="red",
                    pady=20,
                    command=None,
                ).grid(column=0, row=1)
                if self.data["correct"] == 2:
                    self.answer_button_b = Button(
                        self.window,
                        text=self.data["answer2"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=2)
                    self.answer_button_c = Button(
                        self.window,
                        text=self.data["answer3"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=3)
                else:
                    self.answer_button_b = Button(
                        self.window,
                        text=self.data["answer2"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=2)
                    self.answer_button_c = Button(
                        self.window,
                        text=self.data["answer3"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=3)

    def pressed_button_b(self):
        if not (self.active_button == 2):
            self.active_button = 2
            self.answer_button_a = Button(
                self.window,
                text=self.data["answer1"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_a,
            ).grid(column=0, row=1)
            self.answer_button_b = Button(
                self.window,
                text=self.data["answer2"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="yellow",
                pady=20,
                command=self.pressed_button_b,
            ).grid(column=0, row=2)
            self.answer_button_c = Button(
                self.window,
                text=self.data["answer3"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_c,
            ).grid(column=0, row=3)

        elif not self.answered:
            self.answered = True
            if self.data["correct"] == 2:
                self.answer_button_b = Button(
                    self.window,
                    text=self.data["answer2"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="green",
                    pady=20,
                    command=None,
                ).grid(column=0, row=2)
                self.set_main_button("green")
            else:
                self.set_main_button("red")
                self.answer_button_b = Button(
                    self.window,
                    text=self.data["answer2"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="red",
                    pady=20,
                    command=None,
                ).grid(column=0, row=2)
                if self.data["correct"] == 1:
                    self.answer_button_a = Button(
                        self.window,
                        text=self.data["answer1"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=1)
                    self.answer_button_c = Button(
                        self.window,
                        text=self.data["answer3"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=3)
                else:
                    self.answer_button_a = Button(
                        self.window,
                        text=self.data["answer1"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=1)
                    self.answer_button_c = Button(
                        self.window,
                        text=self.data["answer3"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=3)

    def pressed_button_c(self):
        if not (self.active_button == 3):
            self.active_button = 3
            self.answer_button_a = Button(
                self.window,
                text=self.data["answer1"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_a,
            ).grid(column=0, row=1)
            self.answer_button_b = Button(
                self.window,
                text=self.data["answer2"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="grey",
                pady=20,
                command=self.pressed_button_b,
            ).grid(column=0, row=2)
            self.answer_button_c = Button(
                self.window,
                text=self.data["answer3"],
                width=40,
                font=("Arial", 20, "bold"),
                bg="yellow",
                pady=20,
                command=self.pressed_button_c,
            ).grid(column=0, row=3)
        elif not self.answered:
            self.answered = True
            if self.data["correct"] == 3:
                self.answer_button_c = Button(
                    self.window,
                    text=self.data["answer3"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="green",
                    pady=20,
                    command=None,
                ).grid(column=0, row=3)
                self.set_main_button("green")
            else:
                self.set_main_button("red")
                self.answer_button_c = Button(
                    self.window,
                    text=self.data["answer3"],
                    width=40,
                    font=("Arial", 20, "bold"),
                    bg="red",
                    pady=20,
                    command=None,
                ).grid(column=0, row=3)
                if self.data["correct"] == 1:
                    self.answer_button_a = Button(
                        self.window,
                        text=self.data["answer1"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=1)
                    self.answer_button_b = Button(
                        self.window,
                        text=self.data["answer2"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=2)
                else:
                    self.answer_button_a = Button(
                        self.window,
                        text=self.data["answer1"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="grey",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=1)
                    self.answer_button_b = Button(
                        self.window,
                        text=self.data["answer2"],
                        width=40,
                        font=("Arial", 20, "bold"),
                        bg="green",
                        pady=20,
                        command=None,
                    ).grid(column=0, row=2)

    def load_question(self, question_number):
        self.answered = False
        self.data = json.loads(question_number)
        self.set_main_button("grey")
        self.window = Toplevel(width=1920, height=1080)
        img = Image.open(self.data["pic"])
        img = ImageTk.PhotoImage(img)
        Label(self.window, image=img).grid(column=0, row=0)
        self.answer_button_a = Button(
            self.window,
            text=self.data["answer1"],
            width=40,
            font=("Arial", 20, "bold"),
            bg="grey",
            pady=20,
            command=self.pressed_button_a,
        ).grid(column=0, row=1)
        self.answer_button_b = Button(
            self.window,
            text=self.data["answer2"],
            width=40,
            font=("Arial", 20, "bold"),
            bg="grey",
            pady=20,
            command=self.pressed_button_b,
        ).grid(column=0, row=2)
        self.answer_button_c = Button(
            self.window,
            text=self.data["answer3"],
            width=40,
            font=("Arial", 20, "bold"),
            bg="grey",
            pady=20,
            command=self.pressed_button_c,
        ).grid(column=0, row=3)
        self.window.mainloop()


if __name__ == "__main__":
    quiz = Quiz()
