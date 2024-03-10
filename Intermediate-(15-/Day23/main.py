import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
BASE_N_CARS = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key='Up', fun=user.step)

game_is_on = True
frame_counter = 0

car_manager.add_cars(BASE_N_CARS)

while game_is_on:
    frame_counter += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.allcars:
        if abs(user.xcor() - car.xcor()) < 23 and abs(user.ycor() - car.ycor()) < 22:
            game_is_on = False
            scoreboard.roadkill()


    #Detect collision with finish
    if user.ycor() > FINISH_LINE_Y:
        scoreboard.up_level()
        user.starting_line()
        car_manager.up_the_speed()
        car_manager.add_cars(int(BASE_N_CARS/5))

screen.exitonclick()