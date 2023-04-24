import tkinter

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="This is Label", font=("Arial", 24))
my_label.pack()




window.mainloop()
