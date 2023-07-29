import time
import turtle as t
from paddle import Paddle
from ball import Ball
from score import Score

##TODO CREATE SCORE; TRACK SCORE
##TODO CREATE DOTTED SCREEN DIVIDER
##TODO BOUNCING BALL
##TODO DETECT WHEN PADDLE MISS
##TODO BALL COLLIDE WITH PADDLE
##TODO BALL COLLIDES WITH WALL

##TODO CREATE BLACK SCREEN FOR MATCH

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Ultimate Ping Pong Game")
screen.listen()
screen.tracer(0)  # stops animation capability

rpaddle = Paddle((350, 0))  # Paddle((350, 0) = rpaddle.goto(); needs a variable passed thru init to work; must be tuple
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.goup, "w")
screen.onkey(lpaddle.godown, "s")

start = True
while start:
    time.sleep(ball.ballspeed)  # was time.sleep(0.1), but the current code will up speed throughout the game for better experience
    # to slow down ball; atl method is to reduce pixel (10) on ball.py module

    screen.update()  # restarts animation through continuous updates; needs a while loop to work
    ball.move()

# detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# detect collision with paddle; additional condition is needed due to distance() measures from the center of turtle
# additional condition will account for the entire len of paddle

    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# detect when rpaddle misses the ball

    if ball.xcor() > 380:
        ball.resetball()
        score.lpoint()

# detect when lpaddle misses the ball

    if ball.xcor() < -380:
        ball.resetball()
        score.rpoint()





screen.exitonclick()
