import colorgram
import turtle
import random


def get_colors_list(file):
    extract_color = colorgram.extract(file, 15)
    rgbs = []
    for item in extract_color:
        rgbs.append((item.rgb[0],
                     item.rgb[1],
                     item.rgb[2]))
    return rgbs

def get_color(rgbs):
    color = random.choice(rgbs)
    return color


def draw_dots():
    my_turtle.pendown()
    my_turtle.pencolor(color)
    my_turtle.dot(20)
    my_turtle.penup()
    my_turtle.forward(50)


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    turtle.colormode(255)
    my_turtle.speed("fastest")
    colors = get_colors_list("hirst_spot_painting.jpg")
    x_pos = -250
    y_pos = -200
    tries = 0
    while tries <= 10:
        my_turtle.penup()
        my_turtle.setpos(x_pos, y_pos)
        for _ in range(10):
            color = get_color(colors)
            draw_dots()
        tries += 1
        y_pos += 50

    turtle.Screen().exitonclick()

