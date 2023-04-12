from turtle import Turtle


class My_turtle(Turtle):
    def __init__(self, screen):
        super().__init__(shape="turtle")
        self.hideturtle()
        self.penup()
        self.goto(0, -screen.window_height() / 2 + 40)
        self.resizemode("user")
        self.shapesize(2, 2, 1)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(25)
