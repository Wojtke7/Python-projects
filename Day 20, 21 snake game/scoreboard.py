from turtle import Turtle

with open("data.txt") as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.color("white")
        self.penup()
        self.setposition(0, screen.window_height() / 2 - 40)
        self.hideturtle()
        self.change_score()

    def change_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.hideturtle()
        self.setposition(0, 0)
        self.write(f"Game over!", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.change_score()

    def increase_score(self):
        self.score += 1
        self.change_score()
