import turtle
import pandas


def check_states(states_list, answer):
    for i in states_list:
        if i == answer:
            return True
    else:
        return False


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

''' needed to find coordinates of each state '''
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()
print(type(states_names[0]))

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
num_of_states = 0

while True:

    if not states_names or answer_state == "Exit":
        break

    if check_states(states_names, answer_state):
        states_names.pop(states_names.index(answer_state))
        num_of_states += 1
        row = data[data.state == answer_state]
        coordinate_x = int(row.x)
        coordinate_y = int(row.y)
        writing = turtle.Turtle()
        writing.hideturtle()
        writing.penup()
        writing.setposition(coordinate_x, coordinate_y)
        writing.write(f"{row.state.item()}", align="center", font=("Arial", 8, "normal"))

    answer_state = screen.textinput(title=f"{num_of_states} States Correct",
                                    prompt="What's another state's name?").title()

    screen.update()

df = pandas.DataFrame(states_names)
df.to_csv("G:/CODING/100 Days of code Python/Day 25 CSV and Panda library/states_to_learn.csv", index=False, header=False)
