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

    def collision(self, cars):
        for i in cars:
            if abs(i.xcor() - self.xcor()) < 50 and abs(i.ycor() - self.ycor()) < 40:
                return True

    def finish(self, screen):
        if self.ycor() >= screen.window_height() / 2 - 40:
            return True

    def start_pos(self, screen):
        self.hideturtle()
        self.penup()
        self.goto(0, -screen.window_height() / 2 + 40)
        self.showturtle()
