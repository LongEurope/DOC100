from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.shape('circle')
        self.pencolor('white')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_move = 11
        self.y_move = 11
        self.move_interval = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_move *= -1
    
    def hit(self):
        self.x_move *= -1
        self.move_interval *= 0.75
    
    def reposition(self):
        self.ht()
        self.goto(0, 0)
        # self.down()
        # self.write(arg='Resetting ball..', align='center', font=('Arial', 15, 'normal'))
        # time.sleep(1)
        # self.up()
        # self.clear()
        time.sleep(0.2)
        self.st()
        self.move_interval = 0.1
        self.x_move *= -1