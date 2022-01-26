from turtle import Turtle
import random
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard = Scoreboard()

COlORS = ["blue", "green", "Yellow", "red", "orange"]
CarLanes = [y1, y2, y3]


class Level_design(Turtle):

    def __init__(self):
        super.__init__()
        self.scoreboard.increase_level()

    def create_new_cars(self):

        def create_car(self):
            global y1, y2, y3

           # increase how often car is produced
            if scoreboard.self.level() <= 4:
                random_chance = random.randint(1, 6)

            elif scoreboard.self.level() >= 5:
                random_chance = random.randint(1, 5)

            elif scoreboard.self.level() >= 8:
                random_chance = random.randint(1, 4)

            elif scoreboard.self.level() >= 10:
                random_chance = random.randint(1, 3)

            if random_chance == 1:
                new_car = Turtle("square")
                new_car.shapesize(stretch_wid=1, stretch_len=0.5)
                new_car.penup()
                new_car.color(random.choice(COLORS))

                y1 = random.randint(-100, -50)
                y2 = random.randint(-200, -150)
                y3 = random.randint(50, 100)

                new_car.goto(300, random.choice(CarLanes))
                self.all_cars.append(new_car)



                # want to add (append new lane to screen each level and change speed and location of lanes