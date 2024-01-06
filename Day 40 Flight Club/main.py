import sheety

print("Welcome to the Flight Club.")
print("We find the best flight deals and email you")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

email = input("What is your email?\n")
email_check = input("Type your email again\n")

if email == email_check:
    print("You're in the club!")
    sheety.post_user(email, first_name, last_name)
else:
    print("Emails are not the same!")
