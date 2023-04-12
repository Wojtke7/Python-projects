from turtle import Screen
from my_turtle import My_turtle
from cars import Car
import random
import time

start_time = time.time()
interval = 1.5

screen = Screen()
screen.tracer(0)

screen.colormode(255)
eo = My_turtle(screen)
screen.onkey(eo.move, "w")
screen.listen()

cars = []

is_on = True
while is_on:
    screen.update()

    random_range = random.randint(4, 7)

    current_time = time.time()
    if current_time - start_time >= interval:
        for i in range(random_range):
            car = Car(screen)
           # car.check_pos(cars)
            cars.append(car)
            start_time = current_time
    for i in cars:
        i.move()

    time.sleep(0.1)

screen.exitonclick()
