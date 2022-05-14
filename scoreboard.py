from turtle import Turtle

ALIGN= "center"
FONT= ("Verdana", 24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores=0
        self.penup()
        self.goto(-50, 310)
        self.color("white")
        self.createScoreBoard()
        self.hideturtle()
    
    def createScoreBoard(self):
        self.write(f"Scores:{self.scores}", move=False, align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGN, font=FONT)


    def addScores(self, num):
        self.scores=self.scores+num
        self.clear()
        self.createScoreBoard()
    

    