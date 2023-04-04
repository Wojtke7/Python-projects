import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)


TURT_SIZE = 20
start_pos_x = TURT_SIZE / 2 - screen.window_width() / 2 + 15


def move_turt(L):
    for i in L:
        rand_values = random.randint(3, 50)
        i.forward(rand_values)


def set_start_pos(L):
    y_cor = 80
    for i in L:
        i.penup()
        i.goto(start_pos_x, y_cor)
        y_cor -= 40


def check_winner(L, choice):
    for i in L:
        if i.xcor() >= screen.window_width()/2 - TURT_SIZE:
            if i.pencolor() == choice:
                print(f"Turtle {i.pencolor()}, is the winner! You were right!")
                return False
            else:
                print(f"Turtle {i.pencolor()}, is the winner! You lost!")
                return False

    return True


def game():
    set_start_pos(turt_list)
    correct = True
    while correct:
        move_turt(turt_list)
        correct = check_winner(turt_list, chosen_turt)


t1 = Turtle("turtle")
t1.color("red")
t2 = Turtle("turtle")
t2.color("blue")
t3 = Turtle("turtle")
t3.color("yellow")
t4 = Turtle("turtle")
t4.color("purple")
t5 = Turtle("turtle")
t5.color("green")

turt_list = [t1, t2, t3, t4, t5]
chosen_turt = screen.textinput("WINNER", "Choose your winner")

game()

screen.exitonclick()
