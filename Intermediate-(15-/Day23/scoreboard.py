from turtle import Turtle

FONT = ("Arial", 18, "normal")

LEVELPOSITION = (-250, 260)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.up()
        self.speed('fastest')
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(LEVELPOSITION)
        self.write(arg=f'Level: {self.level}', align='center', font=FONT)

    def up_level(self):
        self.level += 1
        self.update_level()
    
    def roadkill(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=("Arial", 48, "normal"))