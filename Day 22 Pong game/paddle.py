from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, side, screen):
        super().__init__()
        self.segments = []
        self.create_paddle(side, screen)
        self.head = self.segments[0]

    # The game could be easier and smoother if I built the paddle using a single stretched square instead of multiple
    # squares.
    def create_paddle(self, side, screen):
        j = 40
        for _ in range(4):
            i = Turtle("square")
            i.hideturtle()
            i.color("white")
            i.resizemode("user")
            i.shapesize(1, 2, 1)
            i.speed(0)
            i.penup()
            i.setheading(90)
            if side == "L":
                i.goto(-screen.window_width() / 2 + 60, j)
                i.showturtle()
                j -= 20
            elif side == "R":
                i.goto(screen.window_width() / 2 - 60, j)
                i.showturtle()
                j -= 20
            self.segments.append(i)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].sety(new_y)
        self.head.forward(40)

    def move_up(self):
        if self.head.ycor() < 290:
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
                self.move()
            else:
                self.segments.reverse()
                self.head = self.segments[0]
                self.setheading(UP)
                self.move()

    def move_down(self):
        if self.head.ycor() > -290:
            if self.head.heading() != UP:
                self.head.setheading(DOWN)
                self.move()
            else:
                self.segments.reverse()
                self.head = self.segments[0]
                self.head.setheading(DOWN)
                self.move()
