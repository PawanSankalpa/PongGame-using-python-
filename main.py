"""importing classes"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""Editor's panel"""
BACKGROUND_COLOR = "Black"
SCREEN_WIDTH  = 900
SCREEN_LENGTH = 600
TITle = "pong game"
RIGHT_SIDE = (SCREEN_WIDTH/2) -25
LEFT_SIDE  =-RIGHT_SIDE
WALL_MARGIN = 281
PADDLE_MARGIN = 408
OUT_ZONE = 430

"""creating the screen"""
screen = Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.setup(SCREEN_WIDTH,SCREEN_LENGTH)
screen.title(TITle)
screen.tracer(0)

"""naming variable"""
right_paddle = Paddle(RIGHT_SIDE)
left_paddle = Paddle(LEFT_SIDE)
ball = Ball()
r_score =Scoreboard(50)
l_score =Scoreboard(-50)

"""giving commands"""
#right paddle movements
screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")

#left paddle movements
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")


"""playing the game"""
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    """detect collision with the top and bottom wall"""
    if ball.ycor() >= WALL_MARGIN or ball.ycor() <= -WALL_MARGIN:
        ball.bounce_y()

    """detect paddle collision and bounce"""
    if ball.distance(right_paddle) < 50 and ball.xcor() > PADDLE_MARGIN or ball.distance(left_paddle) < 50 and ball.xcor() < -PADDLE_MARGIN:
        ball.bounce_x()

    """detect out zone and give marks"""
    if ball.xcor() >= OUT_ZONE:
        l_score.increase_score()
        ball.reset_position()

    if ball.xcor() <= -OUT_ZONE:
        r_score.increase_score()
        ball.reset_position()





screen.exitonclick()