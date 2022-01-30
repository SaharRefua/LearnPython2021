# def foramt_names(f_name, l_name):
#     first = f_name.lower()
#     last = l_name.lower()
#     first[0] = first[0].upper()
#     last[0] = last[0].upper()
#     name = first + " " + last
#     return name
#
#
# first_name = input("Please enter your first name:")
# last_name = input("Please enter your last name:")
#
# formated_name = foramt_names(first_name, last_name)
#
# print(f"Foramted first name is {formated_name}")
#
#
#
from replit import clear
from art_calculator import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()
