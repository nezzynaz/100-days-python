"""Notes on object oriented programming"""

from turtle import Turtle, Screen

# Object oriented programming has classes and objects.
# In this case turt is the object, and the rest is the class
# The class is a blueprint, while the object is an iteration of it.
turt = Turtle()
print(turt)

# Here are some examples of manipulating the turtle using its own methods.
# Methods are functions inside of a class, while attributes are variables and data in classes.
turt.shape("turtle")
turt.color("cyan")
turt.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Python packages are bundles of code created by others for use.
