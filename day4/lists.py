'''Notes on Lists in Python'''
# https://docs.python.org/3/tutorial/datastructures.html
# There's too much information to memorize this, thats why documentation exists.
# Spend more time figuring out how things work and how you want to use it.

# List is a datastructure, and it lets you store items inside that have any data type.
# This is an example of a list, using brackets.
fruits = ["apple", "pear", "banana"]

# The order of items in a list is important for accesing them. The first item is at 0.
# the "index" [0] is where you access the information. 
print(fruits[0])

#This can be negative too, counting backwards.
print(fruits[-2])

# List items can be changed
fruits[1] = "orange"

# Or items can be added (appended) or "extended" (allows another list to be added)
fruits.append("pear")
