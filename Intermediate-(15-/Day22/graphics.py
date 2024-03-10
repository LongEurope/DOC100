from turtle import Turtle

FONT_SIZE = 50

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pencolor('white')
        self.penup()
        self.speed('fastest')
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    def up_right(self):
        self.r_score += 1
        self.update()
    
    def up_left(self):
        self.l_score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align = 'center', font=('Arial', FONT_SIZE, 'normal'))
        self.goto(100, 200)
        self.write(arg=self.r_score, align = 'center', font=('Arial', FONT_SIZE, 'normal'))

class DividingLine(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.pencolor('white')
        self.pensize(3)
        self.ht()
        self.up()
        self.goto(0, 320)
        self.setheading(270)
        for _ in range(20):
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)