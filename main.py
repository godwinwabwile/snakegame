from turtle import Screen
from snake import Snake
import time


# crean a screen instance
screen=Screen()
screen.setup(width=600, height=700)
screen.bgcolor("blue")
screen.tracer(0)
screen.title("Snake Game")

# new snake instance
snake = Snake()

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
    
    








screen.exitonclick()
