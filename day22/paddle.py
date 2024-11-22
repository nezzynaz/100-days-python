'''Paddle'''

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        '''Paddle up movement'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''Paddle down movement'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)  
