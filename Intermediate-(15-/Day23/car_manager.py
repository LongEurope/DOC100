#Can control the amount of cars via rolling a number between 1 and 6 and creating a car on 1

from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_mult = 1
        self.allcars = []
    
    def add_cars(self, n_cars):
        for _ in range(n_cars):
            car = Turtle(shape='square')
            car.up()
            car.shapesize(stretch_len=2.5, stretch_wid=1)
            car.color(random.choice(COLORS))
            random_x = random.randint(-280, 280)
            random_y = random.randint(-240, 240)
            car.goto(random_x, random_y)
            self.allcars.append(car)

    def move_cars(self):
        for car in self.allcars:
            if car.xcor() < -315:
                random_y = random.randint(-240, 240)
                car.goto(320, random_y)
            else:
                new_x = car.xcor() - 5 * self.move_mult
                car.goto(new_x, car.ycor())
    
    def up_the_speed(self):
        self.move_mult += 0.1