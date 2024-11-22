'''Pong game :3'''

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCR = Screen()
SCR.setup(width=800, height=600)
SCR.bgcolor("black")
SCR.title("Pong!")
SCR.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

SCR.listen()
SCR.onkeypress(l_paddle.go_up, "w")
SCR.onkeypress(l_paddle.go_down, "s")
SCR.onkeypress(r_paddle.go_up, "i")
SCR.onkeypress(r_paddle.go_down, "k")

GAME = True

while GAME:
    SCR.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Bounce ball off walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect if ball hits paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

SCR.exitonclick()
