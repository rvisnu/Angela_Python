import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.speed("fastest")
angle = 0

def random_rgb():
    rand_color = []
    for i in range(3):
        rand_color.append(random.random())
    return tuple(rand_color)


while angle <= 360:
    angle += 5
    my_turtle.circle(100)
    my_turtle.color(random_rgb())
    my_turtle.seth(-angle)

turtle.Screen().exitonclick()