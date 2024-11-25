import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from controls import Controls

SCR = Screen()
SCR.setup(width=600, height=600)
SCR.tracer(0)
SCR.title("Turtle Crossing!")
SCR.bgcolor("darkseagreen2")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
controls = Controls()

SCR.listen()
SCR.onkeypress(player.go_up, "w")
SCR.onkeypress(player.go_down, "s")

GAME_ON = True
while GAME_ON:
    time.sleep(0.1)
    SCR.update()
    controls.show_controls()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            GAME_ON = False
            scoreboard.game_over()

    # Detect finish line
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

SCR.exitonclick()
