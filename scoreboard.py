from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.font_size = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        # self.goto(300, 300)

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align="center", font=("Courier", self.font_size, "normal"))
        if self.score == 45:
            self.clear()
            self.write("You Win!", align="center", font=("Courier", 20, "normal"))

    def r_point(self):
        self.score += 1
        self.update_scoreboard()


