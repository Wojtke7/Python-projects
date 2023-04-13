from turtle import Screen
from my_turtle import My_turtle
from cars import Car
from level_board import Level
import random
import time

start_time = time.time()
interval = 2

screen = Screen()
screen.tracer(0)

screen.colormode(255)
eo = My_turtle(screen)
levels = Level(screen)
screen.onkey(eo.move, "w")
screen.listen()

level = 0.1

cars = []
for i in range(5):
    car = Car(screen)
    cars.append(car)

is_on = True
while is_on:
    screen.update()

    random_range = random.randint(4, 7)

    current_time = time.time()

    if current_time - start_time >= interval:
        for i in range(random_range):
            car = Car(screen)
            cars.append(car)
            start_time = current_time

    for i in cars:
        i.move()

    if eo.collision(cars):
        # It'll be good to correct collisions, to be more visible and understandable
        eo.move()
        screen.update()
        levels.game_over()
        break

    if eo.finish(screen):
        eo.start_pos(screen)
        levels.change_level()

        for i in cars:
            i.hideturtle()
        cars.clear()

        level *= 0.8
        interval *= 0.8

    time.sleep(level)

screen.exitonclick()
