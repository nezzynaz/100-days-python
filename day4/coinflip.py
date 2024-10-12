'''Notes on the random module'''
# https://docs.python.org/3/library/random.html

import random # Imports the random module. A module lets you split code up into individual modules.

COIN = random.randint(0, 1) #pulls randint from the random module, and asks for two integer values.

if COIN == 1:
    print("Tails!")
else:
    print("Heads!")
