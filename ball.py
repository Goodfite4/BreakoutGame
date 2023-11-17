from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 0
        self.y_move = -10
        self.move_speed = 0.03
        self.i = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        if self.i == 0:
            self.x_move = 10
            self.i += 1
            self.y_move *= -1
        else:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 0
        self.y_move = -10
        self.i = 0
        self.bounce_x()




