import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")

paddle1 = Paddle("L", screen)
paddle2 = Paddle("R", screen)
ball = Ball()

screen.listen()
screen.onkeypress(paddle1.move_up, "w")
screen.onkeypress(paddle1.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")

is_on = True
while is_on:
    ball.move()
    if ball.paddle_collision(paddle1, paddle2):
        print("Works")
    if ball.out_of_range(screen):
        print("Works")
    time.sleep(0.01)
    screen.update()

screen.exitonclick()
