'''snake class that is inherits from turtle'''
from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0),(-60,0)]
MOVE_DIST=10
# directions
UP= 90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.addsection(position)
            
    
    def addsection(self, position):
        segment =Turtle("square")
        segment.color("black")
        segment.penup()
        segment.shapesize(stretch_len=0.5, stretch_wid=0.5)
        segment.goto(position)
        self.segments.append(segment)

    def extendSnake(self):
        self.addsection(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x= self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DIST)


    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

