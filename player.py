from turtle import Turtle


class Shredder(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.penup()
        self.turtlesize(stretch_wid=2, stretch_len=2, outline=0)
        self.goto(x=xcor, y=ycor)
        self.y_move = .50
        self.katana_list = []

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def throw_katana(self):
        katana = Turtle()
        katana.shape('arrow')
        katana.color('grey')
        katana.penup()
        katana.goto(self.xcor(), self.ycor())
        self.katana_list.append(katana)

    def delete_katana(self, katana):
        katana.reset()
        self.katana_list.remove(katana)

    def move_katanas(self):
        for katana in self.katana_list:
            if katana.ycor() > 400:
                self.delete_katana(katana)
            new_y = katana.ycor() + self.y_move
            katana.goto(katana.xcor(), new_y)

    def clear_katanas(self):
        self.katana_list = []