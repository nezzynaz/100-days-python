'''Notes on Functions with Inputs'''

# functions with inputs are really cool
# The parenthesis allows you to input a variable to pass inside the function.
# In programming terms, the variable name created in the function is called the "parameter".
# While the variable data is called the "Argument".

# something (parameter) = 123 (argument)

def greet(name): # The name inside the parameter create the variable name.
    print(f"Hello {name}!") # This uses the variable created.

greet("Nezzy") # This calls the function and gives the argument a value of "nezzy"

def life_in_weeks(age):
    weeks_left = (90 * 52) - (age * 52)
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(25)

# Functions can have more than one input

def greet_with(name, location):
    print(f"Hello {name}, how is {location} this time of year?")

# Functions like this are called "positional" because it depends on the order of the parameters.
# Putting in arguments depend on the right order or else it causes issues.
greet_with("Nezzy", "Texas")

# Alternatively, you can create "keyword" arguments, which include the variables in the paremeters.
# This allows for the arguments to be in any order.
greet_with(name="Nezzy", location="Texas")
