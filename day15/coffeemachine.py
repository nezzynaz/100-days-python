'''Coffee Machine Project! Day 15!'''
# My weakest link so far is dictionaries.
# One improvement to make is removing the need to ask for each coin type.

import sys
from data import MENU, resources

PROFIT = 0
SALES = 0
DRINK = ""
CHOSEN_DRINK = ""

def coin_process():
    """Processes individual coins into single monetary value"""
    print("Please insert coins now.")
    total = int(input("How many quarters:\n> ")) * .25
    total += int(input("How many dimes:\n> ")) * .1
    total += int(input("How many nickles:\n> ")) * .05
    total += int(input("How many pennies:\n> ")) * .01
    return total


def report():
    """Reports coffee machines current resource values"""
    print("===Coffee Report===")
    print(f"Water: {resources["water"]}mg")
    print(f"Milk: {resources["milk"]}mg")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${PROFIT}")
    print(f"There have been {SALES} total sales.\n")


def sufficient_resources(order_ingredients):
    """Checks the current values to see if drink is possible."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough resources to create {item}.")
            return False
    return True

def transaction(money, drink_cost):
    """Returns true when payment is accepted, and false if money is insufficient."""
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global PROFIT, SALES
        PROFIT += drink_cost
        SALES += 1
        return True
    else:
        print("Not enough money for transaction. Money refunded.")
        return False

def coffee_creation(drink, order_ingredients):
    """Makes coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink}, enjoy!\n")

def purchase_process(drink_ingredients):
    """Processes the drink making process."""
    money = coin_process()
    can_make = sufficient_resources(drink_ingredients["ingredients"])
    if can_make and transaction(money, DRINK["cost"]) is True:
        coffee_creation(CHOSEN_DRINK, DRINK["ingredients"])
    else:
        return

def main():
    """Main Function."""
    on = True
    global DRINK, CHOSEN_DRINK
    while on:
        print("Welcome to the coffee machine console.")
        print("Input a coffee name to brew, type report, or off.")

        command = input("What would you like? (cappuccino, latte, or espresso?)\n> ").lower()
        if command == "cappuccino":
            CHOSEN_DRINK = list(MENU.keys())[2]
            DRINK = MENU[command]
            purchase_process(DRINK)
        elif command == "latte":
            CHOSEN_DRINK = list(MENU.keys())[1]
            DRINK = MENU[command]
            purchase_process(DRINK)
        elif command == "espresso?":
            CHOSEN_DRINK = list(MENU.keys())[0]
            DRINK = MENU[command]
            purchase_process(DRINK)
        elif command == "report":
            report()
        elif command == "off":
            print("Thank you, goodbye!")
            on = False
        else:
            print("Invalid command!")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit(0)
