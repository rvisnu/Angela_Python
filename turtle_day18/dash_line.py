import turtle

my_turtle = turtle.Turtle()

for i in range(10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()

turtle.Screen().exitonclick()