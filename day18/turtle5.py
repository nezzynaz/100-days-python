'''Next Turtle Challenge. Builds shapes of growing sides with random colors.'''

import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.bgcolor("gainsboro")
screen.colormode(255)
tim.shape("arrow")
tim.width(2)
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

rd = 10

for i in range(500):
    tim.color(random_color())
    tim.circle(200, 360)
    tim.setheading(rd + (i + i))

screen.exitonclick()
