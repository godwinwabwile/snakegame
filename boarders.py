from turtle import Turtle
TOP=340
BOTTOM=-340
LEFTCORD=-290
RIGHTCORD=290
shape= "square"

class Boarder(Turtle):
    def __init__(self):
        super().__init__()
        
        
    def createboarder(self,xcod, ycod, hstretch, wstretch):
        self.penup()
        self.color("black")
        self.shape(shape)
        self.goto(xcod,ycod)
        self.shapesize(stretch_len=hstretch, stretch_wid=wstretch)

    