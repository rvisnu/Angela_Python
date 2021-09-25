from turtle import Turtle
import random
FOOD_COLOR = ["blue", "pink", "yellow", "orange", "red", "green", "white"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.refresh()

    def refresh(self):
        def get_random():
            return random.randint(-270, 270)

        self.color(random.choice(FOOD_COLOR))
        self.setposition(get_random(), get_random())

