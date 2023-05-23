from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.5)
        self.penup()
        self.location = location
        self.goto(self.location[0], self.location[1])

    def up(self):
        x, y = self.position()
        y += 20
        self.goto(x, y)

    def down(self):
        x, y = self.position()
        y -= 20
        self.goto(x, y)
