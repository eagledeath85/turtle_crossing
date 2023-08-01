import random
from turtle import Turtle


class CarManager():

    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    STARTING_MOVE_DISTANCE = 5
    # Increment the car moving speed each time the user levels up
    INCREMENTAL_MOVE = 2

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        # Create a new car approximately 1 out of 6 times
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(CarManager.COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(CarManager.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        CarManager.STARTING_MOVE_DISTANCE += CarManager.INCREMENTAL_MOVE
        for car in self.all_cars:
            car.backward(CarManager.STARTING_MOVE_DISTANCE)