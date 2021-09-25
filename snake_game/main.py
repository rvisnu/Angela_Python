import turtle
import time
from turtle_snake import DrawSnake
from food import Food
from score_board import ScoreBoard
from set_border import SetSquareBorder


# setting screen
scr = turtle.Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
is_game_on = True

# get snake
my_score = ScoreBoard()
SetSquareBorder(275, 275)
my_snake = DrawSnake()
my_food = Food()
scr.tracer(0)

scr.listen()
scr.onkey(my_snake.up, "Up")
scr.onkey(my_snake.down, "Down")
scr.onkey(my_snake.left, "Left")
scr.onkey(my_snake.right, "Right")

while is_game_on:
    scr.update()
    my_snake.move_snake()
    time.sleep(1/15)

    # collision with food
    if my_snake.head.distance(my_food.position()) < 10:
        my_snake.extend_snake()
        my_score.score += 1
        my_score.update_score(my_score.score)
        my_food.refresh()
    if my_snake.head.xcor() > 265 or my_snake.head.xcor() < -265 or \
        my_snake.head.ycor() > 265 or my_snake.head.ycor() < -265:
        is_game_on = False
        my_score.end_game()

    for segment in my_snake.segments:
        if segment == my_snake.head:
            pass
        elif my_snake.head.distance(segment) < 9:
            is_game_on = False
            my_score.end_game()





scr.exitonclick()