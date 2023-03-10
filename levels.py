from ninjas import TurtleSquad


class Level:

    def __init__(self):
        self.ninja_list = []
        self.x_start = -130
        self.y_start = 280

    def switch_dir(self, direction):
        if direction == "left":
            return 'right'
        else:
            return 'left'

    def move_ninjas(self, direction):
        if direction == "left":
            for ninja in self.ninja_list:
                new_x = ninja.xcor() - 1
                ninja.goto(new_x, ninja.ycor())

        if direction == "right":
            for ninja in self.ninja_list:
                new_x = ninja.xcor() + 1
                ninja.goto(new_x, ninja.ycor())

    def load_ninjas(self, level):
        ninja_count = 0
        first_row = self.x_start
        second_row = self.x_start
        third_row = self.x_start
        fourth_row = self.x_start
        if level == 1:
            for i in range(21):
                if i < 10:
                    turtle = TurtleSquad(xcor=first_row, ycor=self.y_start)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    first_row += 50
                if i > 10:
                    turtle = TurtleSquad(xcor=second_row, ycor=220)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    second_row += 50
        if level == 2:
            for i in range(32):
                if i < 10:
                    turtle = TurtleSquad(xcor=first_row, ycor=self.y_start)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    first_row += 50
                if 10 < i < 21:
                    turtle = TurtleSquad(xcor=second_row, ycor=220)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    second_row += 50
                if i > 21:
                    turtle = TurtleSquad(xcor=third_row, ycor=160)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    third_row += 50
        if level == 3:
            for i in range(42):
                if i < 10:
                    turtle = TurtleSquad(xcor=first_row, ycor=self.y_start)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    first_row += 50
                if 10 < i < 21:
                    turtle = TurtleSquad(xcor=second_row, ycor=220)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    second_row += 50
                if 21 < i < 32:
                    turtle = TurtleSquad(xcor=third_row, ycor=160)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    third_row += 50
                if i > 31:
                    turtle = TurtleSquad(xcor=fourth_row, ycor=100)
                    self.ninja_list.append(turtle)
                    ninja_count += 1
                    fourth_row += 50