import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self, screen):
        super().__init__(shape="circle")
        rand_x = random.randint(-screen.window_width() / 2 + 100, screen.window_width() / 2 - 100)
        rand_y = random.randint(-screen.window_height() / 2 + 100, screen.window_height() / 2 - 100)
        self.penup()
        self.color("blue")
        self.setposition(rand_x, rand_y)

    def random_cor(self, screen):
        rand_x = random.randint(-screen.window_width() / 2 + 100, screen.window_width() / 2 - 100)
        rand_y = random.randint(-screen.window_height() / 2 + 100, screen.window_height() / 2 - 100)
        self.hideturtle()
        self.setposition(rand_x, rand_y)
        self.showturtle()

    def check_food(self, snake):
        if abs(snake.segments[0].xcor() - self.xcor()) <= 20 and abs(snake.segments[0].ycor() - self.ycor()) <= 20:
            return True
        else:
            return False
