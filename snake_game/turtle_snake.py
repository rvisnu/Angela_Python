import turtle
BODY_POSITION = [(0, 0), (-10, 0), (-30, 0)]
DISTANCE_TO_MOVE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class DrawSnake:
    def __init__(self):
        self.segments = []
        self.draw_snake()
        self.head = self.segments[0]

    def draw_head(self, position):
        self.head = turtle.Turtle()
        self.head.penup()
        self.head.shape("arrow")
        self.head.color("white")
        self.head.goto(position)
        return self.head

    def draw_body(self, position):
        body = turtle.Turtle()
        body.penup()
        body.pencolor("white")
        body.shape("square")
        body.goto(position)
        body.color("white")
        return body

    def extend_snake(self):
        self.segments.append(self.draw_body(self.segments[-1].position()))

    def draw_snake(self):
        body_pos = BODY_POSITION

        self.segments.append(self.draw_head(body_pos[0]))
        for pos in body_pos[1:]:
            self.segments.append(self.draw_body(pos))

    def move_snake(self):
        for segment in range(len(self.segments)-1, 0, -1):
            new_coordinates = self.segments[segment-1].position()
            self.segments[segment].goto(new_coordinates)
        self.head.forward(DISTANCE_TO_MOVE)

    def _head_and_body_position(self):
        x_cor_head, y_cor_head = self.head.position()
        x_cor_body_pos, y_cor_body_pos = self.segments[2].position()
        return x_cor_head, y_cor_head, x_cor_body_pos, y_cor_body_pos

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
