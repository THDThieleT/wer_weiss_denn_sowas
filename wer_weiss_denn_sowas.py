# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import json

init = "{}"
frage1 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage2 = '{ "pic":"aal.png", "answer1":"neue Antwort1", "answer2":"Baum", "answer3":"elefant", "correct":2}'
frage3 = (
    '{ "pic":"aal.png", "answer1":"12", "answer2":"18", "answer3":"45", "correct":1}'
)
frage4 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage5 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage6 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage7 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage8 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage9 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage10 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage11 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'
frage12 = '{ "pic":"aal.png", "answer1":"Keine", "answer2":"80-90", "answer3":"100-119", "correct":3}'


class Quiz:
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.title("Wer weiß denn sowas???")
        # Set the geometry of Tkinter frame
        self.main_screen.geometry("1920x1080")
        self.main_screen.configure(bg=("dark grey"))

        self.button_1 = Button(
            self.main_screen,
            text="Thema 1",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage1),
        ).grid(column=0, row=0)
        self.button_2 = Button(
            self.main_screen,
            text="Thema 2",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage2),
        ).grid(column=1, row=0)
        self.button_3 = Button(
            self.main_screen,
            text="Thema 3",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage3),
        ).grid(column=2, row=0)
        self.button_4 = Button(
            self.main_screen,
            text="Thema 4",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage4),
        ).grid(column=3, row=0)
        self.button_5 = Button(
            self.main_screen,
            text="Thema 5",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage5),
        ).grid(column=0, row=1)
        self.button_6 = Button(
            self.main_screen,
            text="Thema 6",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage6),
        ).grid(column=1, row=1)
        self.button_7 = Button(
            self.main_screen,
            text="Thema 7",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage7),
        ).grid(column=2, row=1)
        self.button_8 = Button(
            self.main_screen,
            text="Thema 8",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage8),
        ).grid(column=3, row=1)
        self.button_9 = Button(
            self.main_screen,
            text="Thema 9",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage9),
        ).grid(column=0, row=2)
        self.button_10 = Button(
            self.main_screen,
            text="Thema 10",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage10),
        ).grid(column=1, row=2)
        self.button_11 = Button(
            self.main_screen,
            text="Thema 11",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage11),
        ).grid(column=2, row=2)
        self.button_12 = Button(
            self.main_screen,
            text="Thema 12",
            height=5,
            width=20,
            font=("Arial", 20, "bold"),
            bg="light blue",
            command=lambda: self.load_question(frage12),
        ).grid(column=3, row=2)

        self.answer_button_a = Button()
        self.answer_button_b = Button()
        self.answer_button_c = Button()
        self.active_button = 0
        self.data = json.loads(init)
        self.buttons = []
        self.window = Toplevel

        self.main_screen.mainloop()

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

        else:
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
            else:
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

        else:
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
            else:
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
        else:
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
            else:
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
        self.data = json.loads(question_number)
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
