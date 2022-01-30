from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    choice = input(f"What would you like ?{menu.get_items()}: ")

    if choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "off":
        is_on = False
    else:
        drink=menu.find_drink(choice)
        drink_cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(drink)

# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
