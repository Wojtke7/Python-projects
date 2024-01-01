# import smtplib
#


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2003, month=8, day=25)
# print(date_of_birth)

import datetime as dt
import smtplib
import random

testing_mail = "wojciechmarcela7@gmail.com"
testing_password = "rxttlfneryuuujiw"

quotes_list = []
with open(file="quotes.txt", mode="r") as quotes:
    for line in quotes:
        quotes_list.append(line.strip())

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 1:
    random_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=testing_mail,
                         password=testing_password)
        connection.sendmail(from_addr=testing_mail, to_addrs="Emi.foltyn@interia.pl",
                            msg=f"Subject:Random quote\n\n{random_quote}")
