from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Classic Snake")
my_screen.tracer(0)


snake = Snake()
food = Food()
score_board = Scoreboard()

my_screen.listen()
my_screen.onkeypress(fun=snake.up, key="w")
my_screen.onkeypress(fun=snake.down, key="s")
my_screen.onkeypress(fun=snake.left, key="a")
my_screen.onkeypress(fun=snake.right, key="d")


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score_board.new_scoreboard()
        food.refresh()
        snake.extend_snake()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

my_screen.exitonclick()
