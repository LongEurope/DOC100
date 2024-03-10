from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from graphics import ScoreBoard, DividingLine

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer()
game_is_on = True

paddle_1 = Paddle(350)
paddle_2 = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()
touching_paddle_1 = False
touching_paddle_2 = False

dividing_line = DividingLine()


screen.listen()

screen.onkey(key='Up', fun=paddle_1.up)
screen.onkey(key='Down', fun=paddle_1.down)
screen.onkey(key='w', fun=paddle_2.up)
screen.onkey(key='s', fun=paddle_2.down)

while game_is_on:
    time.sleep(ball.move_interval)
    screen.update()
    ball.move()

    #Detect wall
    if abs(ball.ycor()) > 280:
        ball.bounce()
    
    #Detect paddle
    if abs(ball.xcor() - paddle_1.xcor()) < 12 and abs(ball.ycor() - paddle_1.ycor()) < 52:
        touching_paddle_1 = True
    elif abs(ball.xcor() - paddle_2.xcor()) < 12 and abs(ball.ycor() - paddle_2.ycor()) < 52:
        touching_paddle_2 = True
    
    if touching_paddle_1 or touching_paddle_2:
        ball.hit()
        touching_paddle_1 = False
        touching_paddle_2 = False
    
    #Detect out of bounds
    if ball.xcor() > 410:
        scoreboard.up_left()
        ball.reposition()
    elif ball.xcor() < -410:
        scoreboard.up_right()
        ball.reposition()

screen.exitonclick()