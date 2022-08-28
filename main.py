from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()

score = Scoreboard()



screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()
        score.add_points()
        place = snake.head.pos()
        snake.segment_add()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.resets()
        snake.reset()

    for item in snake.segments[1:]:
        if snake.head.distance(item) < 10:
            score.resets()
            snake.reset()




screen.exitonclick()


