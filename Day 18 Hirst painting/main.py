from turtle import *
from random import choice
from list_of_colors import color_list

screen = Screen()
TURTLE_SIZE = 20
colormode(255)
star_pos_x = TURTLE_SIZE / 2 - screen.window_width() / 2 + 15
star_pos_y = -screen.window_height() / 2 + 2 * TURTLE_SIZE / 2


def draw_circle():
    color1 = choice(color_list)
    eo.color(color1)
    eo.speed(0)
    eo.begin_fill()
    eo.circle(20)
    eo.end_fill()


def next_hop():
    space = 80
    width = screen.window_width()
    height = screen.window_height()
    for j in range(int(height / space)):
        eo.penup()
        eo.goto(star_pos_x, star_pos_y + space * j)
        eo.pendown()
        for i in range(int(width / space)):
            draw_circle()
            eo.penup()
            eo.forward(space)
            eo.pendown()


eo = Turtle(shape="turtle", visible=False)
eo.penup()
eo.goto(star_pos_x, star_pos_y)
eo.pendown()
eo.showturtle()

next_hop()

screen.exitonclick()
