from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem("latte", 200, 150, 24, 2.5)
espresso = MenuItem("espresso", 50, 0, 18, 1.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)


def coffe_machine():
    items = Menu()
    coffe_maker = CoffeeMaker()
    machine = MoneyMachine()

    while True:
        print("What would you like to order? ", items.get_items())
        choice = input()
        if choice == "off":
            break
        elif choice == "report":
            coffe_maker.report()
            machine.report()
        else:
            chosen_coffe = items.find_drink(choice)
            if chosen_coffe is not None:
                if coffe_maker.is_resource_sufficient(chosen_coffe) and machine.make_payment(chosen_coffe.cost):
                    coffe_maker.make_coffee(chosen_coffe)


coffe_machine()
