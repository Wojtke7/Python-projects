from CoffeTypes import MENU, resources


def chosen_operation():
    choice = input("What would you like? (espresso/latte/capuccino)")
    return choice


def another_operations(operation, money):
    if operation == "off":
        return False
    elif operation == "report":
        for key, value in resources.items():
            new_key = key.capitalize()
            print(f"{new_key}: {value}")
        print("Money: ", "$", money, sep="")
    elif operation == "espresso" or operation == "latte" or operation == "cappuccino":
        return True
    else:
        print("Unknown order, try again")


def check_if_available(choice):
    if MENU[choice]["ingredients"]["water"] <= resources["water"]:
        pass
    else:
        print("Sorry there is not enough water.")
        return False

    if MENU[choice]["ingredients"]["coffee"] <= resources["coffee"]:
        pass
    else:
        print("Sorry there is not enough coffee.")
        return False

    if "milk" in MENU[choice]:
        if MENU[choice]["ingredients"]["milk"] <= resources["milk"]:
            pass
        else:
            print("Sorry there is not enough milk.")
            return False
    return True


def change_resources(choice):
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    if "milk" in MENU[choice]:
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]


def process_coins():
    print("Insert coins, tell me, how many quarters, dimes, nickles or pennies you have")
    quarters_amount = float(input("quarters: "))
    dimes_amount = float(input("dimes: "))
    nickles_amount = float(input("nickles: "))
    pennies_amount = float(input("pennies: "))

    summary = quarters_amount * 0.25 + dimes_amount * 0.10 + nickles_amount * 0.05 + pennies_amount * 0.01

    return summary


def check_transaction(summary, choice):
    if MENU[choice]["cost"] < summary:
        change = summary - MENU[choice]["cost"]
        print("Here is $", round(change, 2), " dollars in change", sep="")
        print(f"Here is your {choice.capitalize()}. Enjoy!")
        return True
    elif MENU[choice]["cost"] == summary:
        print(f"Here is your {choice.capitalize()}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffe_machine():
    on = True
    money = 0
    while on:
        while True:
            choice1 = chosen_operation()
            on = another_operations(choice1, money)
            if on is False:
                break
            elif on is None:
                continue
            else:
                break
        if on:
            availability = check_if_available(choice1)
            if availability:
                summary = process_coins()
                availability = check_transaction(summary, choice1)
                if availability:
                    money += MENU[choice1]["cost"]
                    change_resources(choice1)


coffe_machine()
