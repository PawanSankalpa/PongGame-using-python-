"""import functions"""
from turtle import Turtle

"""Editor panel"""
SHAPE = "circle"
COLOR = "white"
MOVING_DISTANCE = 10

"""Creating a class"""
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.x_move = MOVING_DISTANCE
        self.y_move = MOVING_DISTANCE
        self.move_speed =0.1

    """creating a move method"""
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.speed(self.move_speed)
        """starting movements"""
        self.goto(new_x,new_y)

    """creating a bounce method"""
    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 2

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)





