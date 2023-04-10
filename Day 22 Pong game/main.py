import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(10)

paddle1 = Paddle("L", screen)
paddle2 = Paddle("R", screen)
ball = Ball()
scoreboard = Scoreboard(screen)

screen.listen()
screen.onkeypress(paddle1.move_up, "w")
screen.onkeypress(paddle1.move_down, "s")
screen.onkeypress(paddle2.move_up, "Up")
screen.onkeypress(paddle2.move_down, "Down")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.paddle_collision(paddle1, paddle2):
        ball.paddle_bounce()
    if ball.sides_collision(screen):
        ball.side_bounce()
    if ball.out_of_range(screen):
        scoreboard.change_score(ball)
        ball.reset_position()


screen.exitonclick()
