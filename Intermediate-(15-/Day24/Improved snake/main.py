#! there is a tech to kill yourself by 180ing within a frame.

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def dead():
    scoreboard.reset_game()
    snake.reset_game()
    food.refresh(snake.segments)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black') #Background colour
screen.title('Snake') #Title
screen.tracer(0) #Prevents from refreshing screen automatically

snake = Snake()
food = Food(snake.segments)
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='d', fun=snake.right)

screen.update() #Updates screen

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()

    #Checking food
    if snake.head.distance(food) < 5:
        food.refresh(snake.segments)
        scoreboard.upscore()
        snake.extend()
    
    #Checking wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        dead()
    
    #Checking self
    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 5:
            dead()




screen.exitonclick()