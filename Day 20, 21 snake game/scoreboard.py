from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, screen.window_height() / 2 - 40)
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def change_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.hideturtle()
        self.setposition(0, 0)
        self.write(f"Game over!", align="center", font=("Arial", 24, "normal"))
