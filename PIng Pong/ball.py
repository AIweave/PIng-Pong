from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.xmove = 10
        self.ymove = 10
        self.ballspeed = 0.1  # can't use .speed because that's a Turtle attribute

    def move(self):
        movex = self.xcor() + self.xmove
        movey = self.ycor() + self.ymove
        self.goto(x=movex, y=movey)

    def bounce_y(self):
        self.ymove *= -1  # will create an inverse move (pos(10)x neg(-10) = neg); this is the only coordinate to move

    def bounce_x(self):
        self.xmove *= -1
        self.ballspeed *= 0.9  # will increase speed by multiplying it by a number

    def resetball(self):
        self.goto(0, 0)
        self.ballspeed = 0.1  # resets the speed
        self.bounce_x()  # go opposite of current xcor
