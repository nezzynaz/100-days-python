'''Pretty art with turtle graphics'''
# Turtle Documentation https://docs.python.org/3/library/turtle.html
# Turtle Colors https://cs111.wellesley.edu/reference/colors

# import turtle
# You can import a specific module with
# from turtle import Turtle, or import everything with *

# You can also import a module with an alias, eg
# import turtle as t
# This is useful for long module names

from turtle import Turtle, Screen

# If importing a class from a full module, it would be module.class instead of just class.
tim = Turtle()
tim.shape("turtle")
tim.color("cyan")

for _ in range(4):
    tim.forward(100)
    tim.left(90)
















screen = Screen()
screen.exitonclick()
