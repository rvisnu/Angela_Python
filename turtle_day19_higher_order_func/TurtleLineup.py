import turtle
import random


class TurtleLineup:
    def __init__(self, shape, color, x_pos, y_pos):
        self.my_turtle = turtle.Turtle()
        self.my_turtle.penup()
        self.my_turtle.shape(shape)
        self.my_turtle.color(color)
        self.my_turtle.goto(x_pos, y_pos)

    def move_forward(self, paces):
        self.my_turtle.forward(paces)
        return self.my_turtle.position()


if __name__ == "__main__":
    color_choices = ["red", "blue", "pink", "black", "green", "orange"]
    turtle_dict = {}
    x_pos = -230
    y_pos = 220

    We_have_a_winner = False

    scr = turtle.Screen()
    scr.setup(width=500, height=480)
    user_choice = scr.textinput(title="What is your call?",
                                prompt=f"Guess who will win?\npick a color from below\n{color_choices}")
    for _ in range(6):
        y_pos -= 80
        turtle_dict[color_choices[_]] = TurtleLineup(shape="turtle",
                                                     color=color_choices[_],
                                                     x_pos=x_pos,
                                                     y_pos=y_pos)
    while not We_have_a_winner:
        for turtles in turtle_dict:
            if turtle_dict[turtles].move_forward(random.randint(1, 10))[0] >= 230:
                We_have_a_winner = True
                if turtles == user_choice:
                    print(f"you won!{turtles} color turtle reached the goal first!")
                else:
                    print(f"you lost!{turtles} color turtle reached the goal first!")
    scr.exitonclick()