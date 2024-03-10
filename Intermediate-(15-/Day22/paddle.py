from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_coordinate):
        super().__init__()
        self.x = x_coordinate
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed('fastest')
        self.penup()
        self.goto(x_coordinate, 0)
    
    def up(self):
        if self.ycor() < 250:
            self.goto(self.x, self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.x, self.ycor() - 20)