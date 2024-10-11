'''Coding Exercise, ordering a fake pizza in python'''

print("Welcome to Nezzy's Pizza Parlor!")

SIZE = input("What size pizza do you want? (S,M,L)")
PEPPERONI = input("Do you want pepperoni on your pizza? Y/N")
EXTRA_CHEESE = input("Do you want extra cheese? Y/N")

TOTAL = 0
INVALID = "Invalid input, please try again."

# An example of an elseif statement.
if SIZE == "S":
    TOTAL+=15 # += Adds the number to the value, while =+ causes issues.
    # Python believes =+ equals x =+ 1 as x = +1, instead of adding to the variable.
elif SIZE == "M":
    TOTAL+=18
elif SIZE == "L":
    TOTAL+=25
else:
    print(INVALID)

# An example of nested if statements.
if PEPPERONI == "Y":
    if SIZE == "S":
        TOTAL+=2
    else:
        TOTAL+=3
else:
    print(INVALID)

if EXTRA_CHEESE == "Y":
    TOTAL += 1
else:
    print(INVALID)

print(f"Your total today will be ${TOTAL}.")
