'''Turtle race project using turtle graphics'''

import turtle as t
import random
from tkinter import messagebox as mb

IS_RACE_ON = False
screen = t.Screen()
screen.title("Turtle Racing!")
screen.setup(height=400, width=500)

user_bet = screen.textinput("Make a bet!", "Which turtle will win the race (Orange, Red, etc!)")
print(user_bet)

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
y_positions =[-70, -40, -10, 20, 50, 80]
all_turts = []



for i in range (0, 6):
    turt = t.Turtle(shape="turtle")
    turt.color(colors[i])
    turt.penup()
    turt.goto(-230, y_positions[i])
    turt.shape("turtle")
    all_turts.append(turt)

if user_bet:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turt in all_turts:
        if turt.xcor() > 220:
            winning_color = turt.pencolor()
            IS_RACE_ON = False
            if winning_color == user_bet:
                mb.showinfo(title="Race over!", message=f"You've won! The {winning_color} turtle is the winner!")
                # print(f" You've won! The {winning_color} turtle is the winner!")
            else:
                mb.showinfo(title="Race over!", message=f"You've lost! The {winning_color} turtle is the winner!")
                # print(f" You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turt.forward(rand_distance)

screen.exitonclick()

#while True:
#    screen.update()
