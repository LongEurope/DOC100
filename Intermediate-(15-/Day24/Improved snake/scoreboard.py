from turtle import Turtle
import time

file_address = r'C:\Users\gogle\OneDrive\Documents\Python\DOC100\Intermediate-(15-\Day24\highscore.txt'

ALIGNMENT = 'center'
FONT_SIZE = 15

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.up()
        self.pencolor('white')
        self.score = 0
        with open(file_address, mode='r') as file:
            self.high_score = int(file.read())
        self.update_scoreboard()
    
    def upscore(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f'Score: {self.score}    |   High Score: {self.high_score}', align=ALIGNMENT, font=('Arial', FONT_SIZE, 'normal'))
    
    def reset_game(self):  
        if self.score > self.high_score:
            with open(file_address, mode='w') as file:
                self.high_score = self.score
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        for second in range(3, 0, -1):
            self.clear()
            self.update_scoreboard()
            self.goto(0, 0)
            self.write(arg=f'GAME OVER', align=ALIGNMENT, font=('Arial', FONT_SIZE * 2, 'normal'))
            self.goto(0, -50)
            self.write(arg=f'Starting again in {second}', align=ALIGNMENT, font=('Arial', FONT_SIZE * 2, 'normal'))
            time.sleep(1)
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'GAME OVER', align=ALIGNMENT, font=('Arial', FONT_SIZE * 2, 'normal'))