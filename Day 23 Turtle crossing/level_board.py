from turtle import Turtle


class Level(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.setposition(-screen.window_width() / 2 + 80, screen.window_height() / 2 - 50)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 25, "normal"))

    def change_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 25, "normal"))

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game over!", align="center", font=("Arial", 45, "normal"))
