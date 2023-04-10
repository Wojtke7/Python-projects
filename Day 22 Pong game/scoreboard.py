from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.lines = []
        self.create_rectangles(screen)
        self.left_score = 0
        self.right_score = 0

        self.l_score = Turtle()
        self.l_score.hideturtle()
        self.l_score.color("white")
        self.l_score.penup()
        self.l_score.setposition(-100, screen.window_height() / 2 - 120)
        self.l_score.write(f"{self.left_score}", align="center", font=("Arial", 60, "normal"))

        self.r_score = Turtle()
        self.r_score.hideturtle()
        self.r_score.color("white")
        self.r_score.penup()
        self.r_score.setposition(100, screen.window_height() / 2 - 120)
        self.r_score.write(f"{self.right_score}", align="center", font=("Arial", 60, "normal"))

    def create_rectangles(self, screen):
        j = 0
        for i in range(13):
            line = Turtle(shape="square")
            line.color("white")
            line.resizemode("user")
            line.shapesize(1.5, 0.2, 1)
            line.penup()
            line.goto(0, screen.window_height() / 2 - j)
            j += 50
            self.lines.append(line)

    def change_score(self, ball):
        if ball.xcor() > 0:
            self.left_score += 1
            self.l_score.clear()
            self.l_score.write(f"{self.left_score}", align="center", font=("Arial", 60, "normal"))

        else:
            self.right_score += 1
            self.r_score.clear()
            self.r_score.write(f"{self.right_score}", align="center", font=("Arial", 60, "normal"))
