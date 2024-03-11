#Creating a snake class
from turtle import Turtle
import time
NUMBER_OF_SEGMENTS = 3
MOVE_DISTANCE = 20
MOVE_RATE = 0.1
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset_game(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    
    def create_snake(self): #Could replace a singificant amount of lines of code for the function, but can't bother
        for number in range(NUMBER_OF_SEGMENTS):
            x_value = -20 * (number - 1)
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x_value, 0)
            self.segments.append(new_segment)
            
    
    def extend(self):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        time.sleep(MOVE_RATE)
        for seg_num in range(len(self.segments) - 1, 0, -1): #range is C language, so takes no keywords. start stop step.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(self.segments[seg_num - 1].heading())
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)