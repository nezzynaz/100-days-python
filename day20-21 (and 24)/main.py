'''Snake game!'''

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCR = Screen()
SCR.setup(width=600, height=600)
SCR.bgcolor("black")
SCR.title("Snake Game!")
SCR.tracer(0) # Tracer and update allow you to redraw the screen like a CRT monitor
# It lets you redraw only when an update is needed, making things smoother.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

SCR.listen()
SCR.onkey(snake.up, "w")
SCR.onkey(snake.down, "s")
SCR.onkey(snake.left, "a")
SCR.onkey(snake.right, "d")

GAME_IS_ON = True
while GAME_IS_ON:
    SCR.update()
    time.sleep(0.125)
    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

        # detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

SCR.exitonclick()
