import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


### CONTROLING THE TURTLE ###
# Listening to the keys tapped
screen.listen()
screen.onkey(fun=player.go_up, key="Up")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    # Create a new car
    car_manager.create_car()
    car_manager.move()
    # Detect collision between turtle and car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            is_game_on = False
    # Detect successful crossing
    if player.has_reach_finish_line():
        scoreboard.increase_level()
        player.initial_position()
        car_manager.increase_speed()


screen.exitonclick()



