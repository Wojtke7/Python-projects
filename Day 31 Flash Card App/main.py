from tkinter import *
import random
import pandas

GREEN = "#b1ddc6"
# ------------------------- READING DATA ------------------------ #
df = pandas.read_csv("english_polishWords.csv")
words_dict = df.to_dict(orient="records")
print(words_dict)


def random_word():

    random_position = random.choice(words_dict)
    english_word = random_position["English"]

    canvas.itemconfig(language, text=f"English", fill="black")
    canvas.itemconfig(word, text=f"{english_word}", fill="black")
    canvas.itemconfig(displaying_img, image=card_front)

    window.after(3000, flip_card, random_position)


def flip_card(random_position):

    polish_word = random_position["Polish"]

    canvas.itemconfig(displaying_img, image=card_back)
    canvas.itemconfig(language, text=f"Polish", fill="white")
    canvas.itemconfig(word, text=f"{polish_word}", fill="white")


# -------------------------- DESIGN ---------------------------- #
# Create window
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=GREEN)

# Create Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=GREEN)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

displaying_img = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="English", font=("Ariel", 35, "italic"))
word = canvas.create_text(400, 253, text="word", font=("Ariel", 55, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Correct button
corr_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=corr_button_img, highlightthickness=0, command=random_word)
correct_button.grid(row=1, column=1)

# Wrong button
wr_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wr_button_img, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)

random_word()
window.mainloop()
