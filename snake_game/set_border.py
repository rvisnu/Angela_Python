import turtle


class SetSquareBorder:
    def __init__(self, x_end, y_end):
        my_turtle = turtle.Turtle()
        my_turtle.color("white")
        my_turtle.speed("fast")
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.setpos(-x_end, y_end)
        my_turtle.pendown()
        my_turtle.setpos(x_end, y_end)
        my_turtle.setpos(x_end, -y_end)
        my_turtle.setpos(-x_end, -y_end)
        my_turtle.setpos(-x_end, y_end)
