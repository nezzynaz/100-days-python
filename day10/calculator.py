'''Calculator Project for Day 10'''

import sys
LOGO = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies both numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divides both numbers."""
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def main():
    """Main Calculator Program"""
    print(LOGO)
    mathing = True
    num1 = float(input("What is the first number?:\n> "))

    while mathing:
        print("welcome to Nezzy's Calculator!")
        num2 = float(input("What is the next number?:\n> "))
        for symbol in calculations:
            print(symbol)
        calculation_symbol = input("What do you want to calculate?\n> ")
        answer = calculations[calculation_symbol](num1, num2)
        print(f"{num1}{calculation_symbol}{num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n> ")

        if choice == "y":
            num1 = answer
        else:
            mathing = False
            print("\n" * 20)
            main()

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit(0)
