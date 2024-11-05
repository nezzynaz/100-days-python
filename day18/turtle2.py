'''Next Turtle Challenge'''

from turtle import Turtle, Screen

tim = Turtle()

def dashedline():
    for _ in range(10):
        tim.penup()
        tim.forward(10)
        tim.pendown()
        tim.forward(10)

dash = 0

for _ in range(4):
    dashedline()
    tim.left(90)

screen = Screen()
screen.exitonclick()
