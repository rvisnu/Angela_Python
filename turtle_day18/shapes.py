import turtle
import random

my_turtle = turtle.Turtle()

def random_rgb():
    rand_color = []
    for i in range(3):
        rand_color.append(random.random())
    return tuple(rand_color)


for sides in range(3, 11):
    angle = 360/sides
    complete_angle = 360
    my_turtle.pencolor(random_rgb())
    while complete_angle > 0:
        my_turtle.forward(100)
        my_turtle.right(angle)
        complete_angle -= angle

turtle.Screen().exitonclick()