from tkinter import *
window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="This is Label", font=("Arial", 24))
my_label.grid(column=0, row=0)


# Button

def button_clicked():
    inserted_text = input.get()
    my_label.config(text=inserted_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=2)

# Second button

button2 = Button(text="Lol")
button2.grid(row=0, column=3)

# Entry

input = Entry(width=10)
input.grid(row=3, column=4)
input.get()


window.mainloop()
