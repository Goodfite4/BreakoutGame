from turtle import Turtle


class Lives(Turtle):
    def __init__(self):
        self.font_size = 20
        self.life = 3
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.write(f"lives:{self.life}", align="center", font=("Courier", self.font_size, "normal"))
        if self.life == 0:
            self.clear()
            self.write("You Lose", align="center", font=("Courier", self.font_size, "normal"))

    def lose_life(self):
        self.life -= 1
        self.update_lives()

