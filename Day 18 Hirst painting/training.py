import random
from turtle import Turtle
from turtle import Screen

eo = Turtle()


def random_color():
    tuple1 = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    return tuple1


def shapes():
    number_of_sides = 3
    for j in range(9):
        for i in range(number_of_sides):
            eo.forward(100)
            eo.right(360 / number_of_sides)
        number_of_sides += 1
        eo.color(random_color())


def random_walk():
    list_of_directions = [0, 90, 180, 270]
    eo.speed(7)
    eo.width(8)
    for i in range(200):
        eo.color(random_color())
        eo.forward(30)
        eo.setheading(random.choice(list_of_directions))


def drawing_circles(size_of_gap):
    eo.speed(0)
    for i in range(int(360 / size_of_gap)):
        eo.color(random_color())
        eo.circle(100)
        eo.setheading(eo.heading() + size_of_gap)


# shapes()
# random_walk()
drawing_circles(5)

screen = Screen()
screen.exitonclick()
