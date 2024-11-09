'''Etch-a-Sketch project using turtle graphics'''

import turtle as t

tim = t.Turtle()
tim.shape("arrow")
tim.speed(0)
tim.pensize(2)

screen = t.Screen()
screen.title("Etchy-Sketchy")
screen.setup(500, 500)
screen.tracer(0)

MOVE_DISTANCE = 10

def up():
    tim.forward(MOVE_DISTANCE)

def down():
    tim.backward(MOVE_DISTANCE)

def left():
    new_heading = tim.heading() + 20
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 20
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Keybindings
screen.listen()

screen.onkeypress(up, "w")
screen.onkeypress(left, "a")
screen.onkeypress(down, "s")
screen.onkeypress(right, "d")
screen.onkey(clear_screen, "c")

while True:
    screen.update()