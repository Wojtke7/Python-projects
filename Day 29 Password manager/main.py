from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def random_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0 or len(email_entry.get()) == 0:
        messagebox.showinfo(title="Warning", message="There is a missing argument")
    else:
        website_name = website_entry.get()
        email_name = email_entry.get()
        password = password_entry.get()
        new_data = {
            website_name: {
                "email": email_name,
                "password": password,
            }
        }

        msg_box = messagebox.askokcancel(title=website_name,
                                         message=f"These are the details entered: \nEmail: {email_name} \n"
                                                 f"Password: {password} \nIs it ok to save ?")

        if msg_box:

            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                # Saving updated data
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def generate_password():
    password_entry.delete(0, END)
    generated_password = random_password()
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


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

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="nw")

# Add
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="nw")

window.mainloop()
