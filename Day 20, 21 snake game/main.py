from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen1 = Screen()
screen1.tracer(0)
screen1.bgcolor("black")
screen1.listen()
screen1.onkeypress(lambda: eo.mv_left(), "a")
screen1.onkeypress(lambda: eo.mv_right(), "d")
screen1.onkeypress(lambda: eo.up(), "w")
screen1.onkeypress(lambda: eo.down(), "s")

score = Scoreboard(screen1)
eo = Snake()
food = Food(screen1)

is_on = True
while is_on:
    eo.move()
    if food.check_food(eo):
        food.random_cor(screen1)
        score.change_score()
        eo.add_piece()

screen1.exitonclick()
