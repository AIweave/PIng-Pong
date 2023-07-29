from turtle import Turtle


##TODO CREATE PADDLES (20l x 100w)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # don't use self."paddle", just self.
        self.goto(position)  # give xcor, ycor in main.py
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # turtle pixels are 20x20, so w: 5x20 = 100w & l: 1x20 = 20l
        self.pu()

    def up(self):
        newy = self.ycor() + 20  # new y.cor is the current ycor + 20 pixels up, not forward+
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20  # new y.cor is the current ycor - 20 pixels down, not back
        self.goto(self.xcor(), newy)

    def goup(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def godown(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)
