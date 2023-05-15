from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import csv


# ---------------------------- FINDING PASSWORD ------------------------------- #
def find_password():
    website_name = website_entry.get()

    try:
        with open("dane.csv", "r", newline="") as csv_file:
            # Reading old data
            csv_reader = csv.DictReader(csv_file, delimiter=";")

            for row in csv_reader:
                if row["Website"] == website_name:
                    email = row["Email"]
                    password = row["Password"]
                    date = row["Expiring date"]
                    messagebox.showinfo(title="Info",
                                        message=f"Website name: {website_name} \nE-mail: {email} \nPassword: {password} \nExpiring date: {date} ")
                    return
            messagebox.showerror(title="Info", message=f"No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Info", message="No data file found")


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
        expiring_date = f"{day_spinbox.get()}.{month_spinbox.get()}.{year_spinbox.get()}"
        date_msgbox = messagebox.askyesno(f"Expiring date",
                                          message=f"Would you like to set expiring date: {expiring_date} ?")

        if not date_msgbox:
            expiring_date = f"Password without expiring date"

        website_name = website_entry.get()
        email_name = email_entry.get()
        password = password_entry.get()

        new_data = {
            website_name: {
                "Email": email_name,
                "Password": password,
                "Expiring date": expiring_date
            }
        }

        msg_box = messagebox.askokcancel(title=website_name,
                                         message=f"These are the details entered: \n\nEmail: {email_name} \n\n"
                                                 f"Password: {password} \n\nExpiring date: {expiring_date} \n\nIs it "
                                                 f"ok to"
                                                 f"save ? ")

        if msg_box:
            header = None
            try:
                with open("dane.csv", "r", newline="") as file:

                    reader = csv.reader(file, delimiter=";")
                    header = next(reader)

            except FileNotFoundError:
                with open("dane.csv", "w", newline="") as file:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerow(["Website", "Email", "Password", "Expiring date"])
                    header = ["Website", "Email", "Password", "Expiring date"]

            finally:
                with open("dane.csv", "a", newline="") as file:

                    writer = csv.writer(file, delimiter=";")

                    if header is None or header != ["Website", "Email", "Password", "Expiring date"]:
                        writer.writerow(["Website", "Email", "Password", "Expiring date"])

                    for website, info in new_data.items():
                        email = info["Email"]
                        password = info['Password']
                        expiring_date = info['Expiring date']
                        writer.writerow([website, email, password, expiring_date])

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

# Canvas
pass_canva = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
pass_canva.create_image(100, 100, image=lock_image)
pass_canva.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

# Email
email_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=30)
email_entry.grid(column=1, row=2, columnspan=2, sticky="nw")
email_entry.insert(0, string="maarcela@op.pl")
# Password
password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")

password_button = Button(text="Generate Password", command=generate_password, width=16)
password_button.grid(column=2, row=3, sticky="nw")

# Add
add_button = Button(text="Add", width=25, command=add)
add_button.grid(column=1, row=5, columnspan=2, sticky="nw")

# Search button
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(column=2, row=1)

# Date label

date_label = Label(text="Expiring date:", font=("Arial", 10, "bold"))
date_label.grid(column=0, row=4)

# Day date spinbox
spinbox_container = Frame(window)
spinbox_container.grid(column=1, row=4, sticky="nw")

day_spinbox = Spinbox(spinbox_container, from_=1, to=31, wrap=True, width=7)
month_spinbox = Spinbox(spinbox_container, from_=1, to=12, wrap=True, width=8)
year_spinbox = Spinbox(spinbox_container, from_=2023, to=2300, wrap=True, width=8)

day_spinbox.grid(row=0, column=0)
month_spinbox.grid(row=0, column=1)
year_spinbox.grid(row=0, column=2)

window.mainloop()
