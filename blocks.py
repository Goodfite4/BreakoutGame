from turtle import Turtle


class Blocks:
    def __init__(self):
        self.all_blocks = []

    def level(self, position):
        new_block = Turtle("square")
        new_block.penup()
        new_block.goto(position)
        new_block.color("white")
        new_block.shapesize(stretch_wid=0.5, stretch_len=2)
        self.all_blocks.append(new_block)
    def move_block(self, block):
        # Move block out of screen if it contacts the ball.
        block.goto(1000, 1000)
