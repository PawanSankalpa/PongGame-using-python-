from turtle import Turtle

WIDTH = 1  #how many times the normal size
LENGTH = 5 #how many times the normal size
COLOR = "white"
SHAPE = "square"


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape(SHAPE)
        self.shapesize(WIDTH,LENGTH)  #turning around so that it can do easily in next functions
        self.setheading(90)
        self.color(COLOR)
        self.goto(position,0)

    """movement functions"""
    def move_up(self):
        self.setheading(90)
        self.forward(15)

    def move_down(self):
        self.setheading(270)
        self.forward(15)



