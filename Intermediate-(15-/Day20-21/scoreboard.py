from turtle import Turtle

ALIGNMENT = 'center'
FONT_SIZE = 15

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.goto(0, 260)
        self.pencolor('white')
        self.score = -1
        self.upscore()
    
    def upscore(self):
        self.clear()
        self.score += 1
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=('Arial', FONT_SIZE, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', align=ALIGNMENT, font=('Arial', FONT_SIZE * 2, 'normal'))