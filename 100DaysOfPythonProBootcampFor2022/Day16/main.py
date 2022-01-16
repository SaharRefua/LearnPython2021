from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
#itme = MenuItem(name, water, milk, coffee, cost)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
choice = input(f"What would you like ?{menu.get_items()}: ")
while is_on:
    if choice == "report":
        print(coffee_maker.report())
    elif choice == "off":
        is_on = False
    else:

        print("OK")
