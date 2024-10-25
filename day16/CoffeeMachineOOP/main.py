'''Coffee Machine Project using OOP.'''
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ON = True

# item = MenuItem()
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print("Welcome to the coffee machine")

while ON:
    selection = menu.get_items()[:-1]
    print(f"Would you like a {selection}?")
    order = input("What would you like?\n> ").lower()
    if order == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif order == "quit":
        ON = False
        print("Goodbye!")
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
