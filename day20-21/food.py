'''food class'''

# The big part of this file is to learn how class inheritence works in OOP.
# In this case, we're making a special turtle thats already set up the way we want, seperate from the main file.

import random
from turtle import Turtle

class Food(Turtle): # By adding Turtle to the args, the food class can inherit from turtle.
    def __init__(self) -> None:
        super().__init__() # This calls the inherited class inside of food. Not always required, but recommended.
        self.shape("circle")
        self.penup()
        self.shapesize(0.65, 0.65)
        self.color("green")
        self.speed("fastest")
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)
        self.refresh()

    def refresh(self):
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)
