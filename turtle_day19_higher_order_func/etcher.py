import turtle

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def rotate_counter_clock():
    tim.left(5)

def rotate_clock():
    tim.right(5)


if __name__ == "__main__":
    tim = turtle.Turtle()
    scr = turtle.Screen()
    scr.listen()

    scr.onkey(move_forward, "w")
    scr.onkey(move_back, "s")
    scr.onkey(rotate_counter_clock, "a")
    scr.onkey(rotate_clock, "d")
    scr.onkey(scr.resetscreen, "c")
    
    scr.exitonclick()


