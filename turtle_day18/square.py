import turtle


def freeze():
    turtle.Screen().exitonclick()


my_turtle = turtle.Turtle()

for i in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

freeze()


