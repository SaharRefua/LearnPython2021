MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,

}
coffee_machine_turn_on = True

# TODO 2: check resources sufficient


def check_resources(user_request):
    order = MENU[user_request]
    ingredients = order["ingredients"]
    for item in ingredients:
        if resources[item] >= ingredients[item]:
            pass #print(f"{resources[item]} >= {ingredients[item]}")
        else:
            print(f"Sorry that's not enough {item}.")
            return False
    return True


# TODO 4: check transaction successfully


def check_money(order):
    cost = MENU[order]["cost"]
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickles = int(input("How many nickles?: "))
    user_pennies = int(input("How many pennies?: "))
    total_user_payment = user_pennies * 0.01 + user_nickles * 0.05 + user_dimes * 0.10 + user_quarters * 0.25
    print(f"Total pyment of ${total_user_payment}")

    if total_user_payment == cost:
        print(f"Total pyment of ${total_user_payment}")
        resources["money"] = total_user_payment
        print(resources["money"])
        return True
    elif total_user_payment > cost:
        change_to_user = round(total_user_payment - cost,2)
        print(f"Here is ${change_to_user} dollars in change.”")
        resources["money"] = cost
        print(resources["money"])
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 5: Make coffee.

def make_coffee(coffee_ordered):
    order = MENU[coffee_ordered]
    ingredients = order["ingredients"]
    for item in ingredients:
        resources[item] = resources[item] - ingredients[item]
        #print(f"{resources[item]} = {resources[item]} - {ingredients[item]}")
    print(resources)
    print(f"Here is your {coffee_ordered} ☕. Enjoy!")
    #print("Your coffee is ready !")


# TODO 1 :print report
while coffee_machine_turn_on:
    user_answer = input("What would you like ? (espresso/latte/cappuccino): ")

    if user_answer == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    elif user_answer == "espresso" or user_answer == "latte" or user_answer == "cappuccino":
        if check_resources(user_answer):
            print("Please insert Money:")
            # TODO 3: Process coins
            if check_money(user_answer):
                make_coffee(user_answer)
        # else:
        #     print("Not resources please try again!")
    elif user_answer == "off":
        coffee_machine_turn_on = False
    else:
        print("You type wrong answer try again")



# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
#