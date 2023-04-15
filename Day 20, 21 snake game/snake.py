from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.speed("fastest")
            square.goto(x, 0)
            x -= 20
            self.segments.append(square)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(21)

    def add_piece(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        i = len(self.segments)
        last_segment = self.segments[i - 1]
        x = last_segment.xcor()
        y = last_segment.ycor()
        heading = last_segment.heading()
        square.goto(x, y)
        square.setheading(heading)
        self.segments.append(square)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def mv_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def mv_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def wall_collision(self, screen):
        if self.head.xcor() >= screen.window_width() / 2 or self.head.xcor() <= -screen.window_width() / 2:
            return True
        elif self.head.ycor() >= screen.window_height() / 2 or self.head.ycor() <= -screen.window_height() / 2:
            return True
        else:
            return False

    def snake_collision(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            if self.segments[0].position() == self.segments[seg_num].position():
                return True
        return False
