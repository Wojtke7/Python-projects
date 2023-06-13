# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import smtplib
import random
import datetime as dt

testing_mail = "wojciechmarcela7@gmail.com"
testing_password = "rxttlfneryuuujiw"

now = dt.datetime.now()
list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

with open("birthdays.csv", "r", newline="") as csv_file:
    df = pd.read_csv(csv_file)

    found_match = False
    list_of_birthday_persons = []

    for index, row in df.iterrows():
        if row["day"] == now.day and row["month"] == now.month:
            found_match = True
            list_of_birthday_persons.append(row["name"])

    if found_match:
        for NAME in list_of_birthday_persons:

            add_col = df['name']
            random_template = random.choice(list_of_letters)
            address = df.loc[add_col == NAME, 'email']
            print(address)

            with open(random_template, mode="r") as file_to_change:
                content = file_to_change.read()

                modified_content = content.replace("[NAME]", NAME)

                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=testing_mail,
                                     password=testing_password)
                    connection.sendmail(from_addr=testing_mail, to_addrs=address,
                                        msg=f"Subject:Happy birthday {NAME}!\n\n{modified_content}")
