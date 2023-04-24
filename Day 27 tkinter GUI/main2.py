from tkinter import *

window = Tk()
window.title("Miles to kilometers converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)

# Miles entry(input)

ml_input = Entry(width=10)
ml_input.grid(column=1, row=0)
# Miles label

ml_label = Label(text="Miles")
ml_label.grid(column=2, row=0)
# equal label

eq_label = Label(text="is equal to")
eq_label.grid(column=0, row=1)
# Km label

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
# Km value

km_value = Label(text="0")
km_value.grid(row=1, column=1)


# Button
def button_clicked():
    inserted_ml = float(ml_input.get())
    kilometers = inserted_ml * 1.6
    km_value.config(text=kilometers)


calc_button = Button(text="calculate", command=button_clicked)
calc_button.grid(row=2, column=1)

window.mainloop()