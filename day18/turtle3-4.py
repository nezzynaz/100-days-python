'''Next Turtle Challenge. Builds shapes of growing sides with random colors.'''

import random
import turtle as t


tim = t.Turtle()
screen = t.Screen()

screen.bgcolor("gainsboro")
screen.colormode(255)
tim.shape("circle")
tim.width(15)
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

direction = [0, 90, 180, 270]
colors = ["red", "blue", "green", "purple", "orange", "yellow", "cyan"]

for _ in range(300):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(direction))

screen.exitonclick()
