from turtle import Turtle

CRL_FONT = ("Courier", 8, "normal")

class Controls(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def show_controls(self):
        self.goto(0, 280)
        self.write("Press W to Move Forward, S to go Backward", align="center", font=CRL_FONT)
