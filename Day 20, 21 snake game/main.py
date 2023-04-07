from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen1 = Screen()
screen1.tracer(0)
screen1.bgcolor("black")

score = Scoreboard(screen1)
eo = Snake()
food = Food(screen1)

screen1.listen()
screen1.onkeypress(lambda: eo.mv_left(), "a")
screen1.onkeypress(lambda: eo.mv_right(), "d")
screen1.onkeypress(lambda: eo.up(), "w")
screen1.onkeypress(lambda: eo.down(), "s")

is_on = True
while is_on:
    screen1.update()
    time.sleep(0.1)
    eo.move()
    if food.check_food(eo):
        food.random_cor(screen1)
        score.change_score()
        eo.add_piece()
    if eo.wall_collision(screen1) or eo.snake_collision():
        break

score.game_over()
screen1.exitonclick()
