from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        pop_window = Toplevel()
        pop_window.title("Warning")
        pop_window.geometry("200x50")
        warning_label = Label(pop_window, text="There is a missing argument!")
        warning_label.pack()
    else:
        website_name = website_entry.get()
        email_name = email_entry.get()
        password = password_entry.get()
        f = open("passwords.txt", "a")
        f.write(f"{website_name} | {email_name} | {password}\n")
        f.close()

        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

# Canva
pass_canva = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
pass_canva.create_image(100, 100, image=lock_image)
pass_canva.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="nw")
website_entry.focus()

# Email
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="nw")
email_entry.insert(0, string="wojtekmarcela@interia.pl")
# Password
password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nw")

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3, sticky="nw")

# Add
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="nw")

window.mainloop()
