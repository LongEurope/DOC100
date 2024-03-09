#Food is subclass, turtle is super class

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, snake_segments):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #Goes from radius 10 circle to radius 5 circle
        self.color('red')
        self.speed('fastest') #So when position is set it moves quickly
        self.refresh(snake_segments)
    
    def refresh(self, snake_segments):
        contradicting_pos = True

        while contradicting_pos:
            contradicting_pos = False
            random_x = -280 + 20*random.randint(0, 28)
            random_y = -280 + 20*random.randint(0, 28)
            for segment in snake_segments:
                if abs(random_x - segment.xcor()) < 5 and abs(random_y - segment.ycor()) < 5:
                    contradicting_pos = True
        
        self.goto(random_x, random_y)