from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class GraphicalInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.points = 0

        # Window
        self.window = Tk()
        self.window.title("True/False game")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # Canva
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Random text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        corr_button_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=corr_button_img, highlightthickness=0, command=self.true_button_click)
        self.correct_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_button_click)
        self.false_button.grid(row=2, column=1)

        # Score label
        self.score = Label(fg="white", text=f"Score: {self.points}", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def false_button_click(self):
        answer = "false"
        if self.quiz.check_answer(answer):
            self.points += 1
            self.score.config(text=f"Score: {self.points}")
            self.change_colour_to_green()
        else:
            self.change_colour_to_red()

    def true_button_click(self):
        answer = "true"
        if self.quiz.check_answer(answer):
            self.points += 1
            self.score.config(text=f"Score: {self.points}")
            self.change_colour_to_green()
        else:
            self.change_colour_to_red()

    def change_colour_to_green(self):
        self.canvas.config(bg="green")
        self.window.after(1000, self.get_next_question)

    def change_colour_to_red(self):
        self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


