from turtle import Turtle


class Ball(Turtle):
    ball_speed = 1

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def out_of_range(self, screen):
        if self.xcor() >= screen.window_width() / 2 or self.xcor() <= -screen.window_width() / 2:
            return True

    def paddle_collision(self, p1, p2):
        for i in p1.segments:
            if abs(self.xcor() - i.xcor()) < 20 and abs(self.ycor() - i.ycor()) < 20:
                return True
        for i in p2.segments:
            if abs(self.xcor() - i.xcor()) < 20 and abs(self.ycor() - i.ycor()) < 20:
                return True
        return False

    def side_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def sides_collision(self, screen):
        if self.ycor() >= screen.window_height() / 2 - 20 or self.ycor() <= -screen.window_height() / 2 + 20:
            return True

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
