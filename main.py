from turtle import Screen
from boarders import Boarder
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time


# crean a screen instance
screen=Screen()
screen.setup(width=600, height=700)
screen.bgcolor("blue")
screen.tracer(0)
screen.title("WEGO Snake Game")

# new snake instance
snake = Snake()

# create food instance

food= Food()

# create scoreboard instance
scoreboard =Scoreboard()
# create game boarders

topboarder= Boarder()
bottomboarder= Boarder()
leftboarder= Boarder()
rightboarder= Boarder()
topboarder.createboarder(0,300,30,1)
bottomboarder.createboarder(0,-340,30,1)
leftboarder.createboarder(-290,-10,1,32)
rightboarder.createboarder(290, -10,1,32)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
play =True

while play:
    # move snake
    screen.update()
    time.sleep(0.1)
    snake.move()
    score=0

    # detect collition with food === feeding snake
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extendSnake()
        score=score+5
        scoreboard.addScores(score)

    # detect collition with wall === game over
    if snake.head.xcor()> 280 or snake.head.xcor() <-280 or snake.head.ycor()> 290 or snake.head.ycor() <-350 :
        play=False
        scoreboard.gameOver()
    
    # detect collition with tail or other segments === game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            play=False
            scoreboard.gameOver()
    


screen.exitonclick()
