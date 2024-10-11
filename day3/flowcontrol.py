'''Notes on Flow Control with if/else and conditional operators'''

# Here is an example of an if/else statement.
height = int(input("What is your neight in cm? ")) # Variable to find height

if height > 120: # The initial if gives the parameters, where if true will run.
    print("You can ride") # This must be indented because this is how python functions.
else: # Notice the else function is at the same indentation as the if line.
    print("You can't ride") # THis is what python runs if it is false.

# Comparison operators (for python) include:
# > greater than, < less than, >= greater than or equal, <= less than or equal
# == Equal to, != Not equal to

# Note that one equal sign assigns a value to a variable,
# where two equal signs checks the value on the left to the right.

if height == 120:
    print("Wow you are 120 cm!")
else:
    print(":3")
