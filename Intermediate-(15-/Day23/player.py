from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('turtle')
        self.setheading(90)
        self.starting_line()

    def starting_line(self):
        self.ht()
        self.goto(STARTING_POSITION)
        self.st()

    def step(self):
        self.forward(MOVE_DISTANCE)