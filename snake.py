from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

SNAKE_HEAD_COLOR = "SeaGreen4"
SNAKE_BODY_COLOR = "purple3"

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.head.color(SNAKE_HEAD_COLOR)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        snake = Turtle(shape="square")
        snake.color(SNAKE_BODY_COLOR)
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)

    def reset(self):
        for snake in self.snake_list:
            snake.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
        self.head.color(SNAKE_HEAD_COLOR)

    def extend_snake(self):
        self.add_snake(self.snake_list[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[seg_num - 1].xcor()
            new_y = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
