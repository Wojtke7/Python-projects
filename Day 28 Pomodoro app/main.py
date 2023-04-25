from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
CHECK_COUNT = 1
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    global REPS, CHECK_COUNT
    REPS = 1
    CHECK_COUNT = 1
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS, CHECK_COUNT
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 2 != 0:
        counting(work_sec)
        timer_label.config(text="Working time", fg=GREEN)
        check_label.config(text=CHECK_COUNT * "✔")
        REPS += 1
        CHECK_COUNT += 1
    elif REPS % 8 == 0:
        counting(long_break_sec)
        timer_label.config(text="Long break", fg=RED)
        REPS += 1
    elif REPS % 2 == 0 and not REPS % 8 == 0:
        counting(short_break_sec)
        timer_label.config(text="Short break", fg=PINK)
        REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counting(seconds):
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if seconds > 0:
        global TIMER
        TIMER = window.after(1000, counting, seconds - 1)


# ---------------------------- UI SETUP ------------------------------- #
# Window


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# counting(5)
# Start button

st_button = Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
st_button.grid(column=0, row=2)

# Reset button

rs_button = Button(text="Reset", bg="white", highlightthickness=0, command=reset_timer)
rs_button.grid(column=2, row=2)

# Timer label

timer_label = Label(fg=GREEN, text="Timer", bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Check Labels

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
