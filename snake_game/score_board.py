from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update_score(self.score)

    def update_score(self, score):
        self.clear()
        self.setposition(0, 280)
        self.write(f"Score : {score}", align="center", font=("Calibri", 12, "bold"))

    def end_game(self):
        self.setposition(0, 0)
        self.color("cyan")
        self.write(f"GAME OVER!", align="center", font=("Calibri", 20, "bold"))
