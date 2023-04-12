from turtle import Turtle
import random
from list_of_colors import color_list


class Car(Turtle):
    def __init__(self, screen):
        super().__init__(shape="square")
        #need to change randint to randomchoice to avoid collisions with eachother
        random_y = random.randint(-screen.window_height() / 2 + 60, screen.window_height() / 2 - 60)
        random_x = random.randint(screen.window_width() / 2 - 120, screen.window_width() / 2 - 60)
        self.hideturtle()
        self.resizemode("user")
        self.shapesize(2, 5, 1)
        self.setheading(180)
        self.penup()
        self.goto(random_x, random_y)
        self.color(random.choice(color_list))
        self.showturtle()
        self.speed(1)

    def move(self):
        self.forward(10)

    def check_pos(self, cars):
        for i in cars:
            if abs(i.ycor() - self.ycor()) <= 40:
                self.sety(i.ycor() + 80)
