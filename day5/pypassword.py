'''Day 5 Project, building a fake password generator'''

# DO NOT USE THIS TO GENERATE PASSWORDS FOR REAL

# I figure there's a much better way to make a password generator using
# other functions built in to Python.

import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
NR_LETTERS= int(input("How many letters would you like in your password?\n"))
NR_SYMBOLS = int(input("How many symbols would you like?\n"))
NR_NUMBERS = int(input("How many numbers would you like?\n"))

# Initialize a variable to hold the password list
PASSWORD = []

# Uses the random.choice function to choose a random letter and append it to the password, to the
# length that the user specifies.
for char in range (0, NR_LETTERS): # Notice the range is 1 to user choice + 1.
# The range can be either (0, NR_LETTERS) or (1, NR_LETTERS + 1), both are valid.
    PASSWORD.append(random.choice(LETTERS)) # Finds a random choice from the list and appends it.
for char in range (0, NR_SYMBOLS):
    PASSWORD.append(random.choice(SYMBOLS))
for char in range (0, NR_NUMBERS):
    PASSWORD.append(random.choice(NUMBERS))

# This scrambles the created password.
print(PASSWORD)
random.shuffle(PASSWORD)
print(PASSWORD)

# This converts the password from a list to a string.
FINALPASS = ""
for num in PASSWORD:
    FINALPASS += num

print(f"Your password is {FINALPASS}")
