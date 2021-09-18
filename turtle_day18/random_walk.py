import turtle
import random


def get_direction():
    index = random.choice((90,180,270,360))
    move = random.choice([my_turtle.forward, my_turtle.backward])
    return index, move


def draw(distance):
    angle, move = get_direction()
    my_turtle.seth(angle)
    move(distance)


def random_rgb():
    rand_color = []
    for i in range(3):
        rand_color.append(random.random())
    return tuple(rand_color)


if __name__ == "__main__":
    distance = 20
    my_turtle = turtle.Turtle()
    my_turtle.pensize(5)
    my_turtle.speed("fastest")
    for _ in range(300):
        my_turtle.pencolor(random_rgb())
        draw(distance)
    turtle.Screen().exitonclick()
