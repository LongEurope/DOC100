#! Shitty code

import os
from turtle import Turtle, Screen
import random

os.system('cls')
print('''
 /$$$$$$$$                    /$$     /$$                 /$$                   /$$     /$$     /$$                    
|__  $$__/                   | $$    | $$                | $$                  | $$    | $$    |__/                    
   | $$ /$$   /$$  /$$$$$$  /$$$$$$  | $$  /$$$$$$       | $$$$$$$   /$$$$$$  /$$$$$$ /$$$$$$   /$$ /$$$$$$$   /$$$$$$ 
   | $$| $$  | $$ /$$__  $$|_  $$_/  | $$ /$$__  $$      | $$__  $$ /$$__  $$|_  $$_/|_  $$_/  | $$| $$__  $$ /$$__  $$
   | $$| $$  | $$| $$  \__/  | $$    | $$| $$$$$$$$      | $$  \ $$| $$$$$$$$  | $$    | $$    | $$| $$  \ $$| $$  \ $$
   | $$| $$  | $$| $$        | $$ /$$| $$| $$_____/      | $$  | $$| $$_____/  | $$ /$$| $$ /$$| $$| $$  | $$| $$  | $$
   | $$|  $$$$$$/| $$        |  $$$$/| $$|  $$$$$$$      | $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$/| $$| $$  | $$|  $$$$$$$
   |__/ \______/ |__/         \___/  |__/ \_______/      |_______/  \_______/   \___/   \___/  |__/|__/  |__/ \____  $$
                                                                                                              /$$  \ $$
                                                                                                             |  $$$$$$/
                                                                                                              \______/ 
      ''')

screen = Screen()
screen.setup(width=500, height=400)
user_turtle = str(screen.textinput(title='Turtle',prompt='Which turtle will win the race? Enter a color: ')).lower()
user_bet = int(screen.textinput(title='Betting', prompt='How much money would you like to bet?\n Warning: You will not be able to withdraw the money after you input the bet. (Input in dollars)'))

class RacingTurtle:
    def __init__(self, color):
        self.turtle = Turtle(shape='turtle') #Assign class as an attribute of a class, bad thing.
        self.turtle.up()
        self.turtle.color(color)

is_race_on = False
redt = RacingTurtle('red')
oranget = RacingTurtle('orange')
yellowt = RacingTurtle('yellow')
greent = RacingTurtle('green')
bluet = RacingTurtle('blue')
purplet = RacingTurtle('purple')

racers = [redt, oranget, yellowt, greent, bluet, purplet]

for number, racer in enumerate(racers):
    y_value = -90 + 30*number
    racer.turtle.goto(x=-230, y=y_value)

if user_turtle:
    is_race_on = True

while is_race_on:
    for turtle in racers:
        random_distance = random.randint(0, 10)
        turtle.turtle.forward(random_distance)
        if turtle.turtle.xcor() > 230:
            os.system('cls')
            is_race_on = False
            winning_turtle = (turtle.turtle.color())
            if winning_turtle[1] == user_turtle:
                print(f'You won, the {user_turtle} turtle won.')
                print(f'${user_bet*9/2} has been added to your account')
            else:
                print(f'You lost, the {winning_turtle[1]} turtle won.')
                print(f'You\'ve lost ${user_bet}.')

screen.exitonclick()