from turtle import Turtle
import random

RANDOM_DESTINATIONS = [0, 180]
RANDOM_WAYS = [45, 135, 225, 315]


class Ball(Turtle):
    ball_speed = 1

    def __init__(self):
        super().__init__(shape="square")
        random_heading = random.choice(RANDOM_DESTINATIONS)
        random_way = random.choice(RANDOM_WAYS)
        self.color("white")
        self.penup()
        self.setheading(random_heading)
        self.left(random_way)

    def move(self):
        self.speed(self.ball_speed)
        self.forward(3)

    def out_of_range(self, screen):
        if self.xcor() >= screen.window_width() / 2 or self.xcor() <= -screen.window_width() / 2:
            return True

    def paddle_collision(self, p1, p2):
        for i in p1.segments:
            if abs(self.xcor() - i.xcor()) < 10 and abs(self.ycor() - i.ycor()) < 10:
                return True
        for i in p2.segments:
            if abs(self.xcor() - i.xcor()) < 10 and abs(self.ycor() - i.ycor()) < 10:
                return True
        return False

    def paddle_bounce(self, p1, p2):
        pass


