from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-300, -300)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 10, "normal"))

    def new_level(self):
        self.level += 1
        self.update_level()
        timer = Turtle()
        timer.color("white")
        timer.penup()
        timer.hideturtle()
        timer.level = 1
        timer.goto(0, 0)
        timer.write("Nice!", align="center", font=("Courier", 30, "normal"))
        time.sleep(1)
        timer.reset()

    def you_lose(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU LOSE", align="center", font=("Courier", 30, "normal"))

    def you_win(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=("Courier", 30, "normal"))

    def play_again(self):
        time.sleep(1)
        self.clear()
        self.write("PLAY AGAIN?\n Type Y or N", align="center", font=("Courier", 30, "normal"))
