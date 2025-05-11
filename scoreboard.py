"""importing turtle module"""
from turtle import Turtle
"""Editor's panel"""
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")

"""creating class"""
class Scoreboard(Turtle):

    def __init__(self,xcor):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.color(COLOR)
        self.goto(xcor,250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


