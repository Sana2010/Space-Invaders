from turtle import Turtle
import random
COLORS = ["red", "orange", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class TurtleSquad(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("turtle")
        self.setheading(270)
        self.penup()
        self.color(COLORS[random.randint(0, 3)])
        self.turtlesize(stretch_wid=2, outline=0)
        self.goto(xcor, ycor)
