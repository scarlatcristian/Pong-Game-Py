from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.height = 50

    def go_up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def go_down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)

    def top(self):
        return self.ycor() + self.height / 2

    def bottom(self):
        return self.ycor() - self.height / 2

    def left(self):
        return self.xcor() - 20

    def right(self):
        return self.xcor() + 20
