import time
from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")

paddle1 = Paddle("L", screen)
paddle2 = Paddle("R", screen)

screen.listen()
screen.onkeypress(paddle1.move_up, "w")
screen.onkeypress(paddle1.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")

is_on = True
while is_on:
    screen.update()
    # time.sleep(0.1)

screen.exitonclick()
