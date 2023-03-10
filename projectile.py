from turtle import Turtle


class Shuriken(Turtle):

    def __init__(self, ninja):
        super().__init__()
        self.shape("triangle")
        self.color("green")
        self.setheading(270)
        if ninja.ycor() < -200:
            self.color('grey')
        self.penup()
        self.goto(ninja.xcor(), ninja.ycor())
        self.y_move = 3
        self.move_speed = 0.1

    def move_shuriken(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)