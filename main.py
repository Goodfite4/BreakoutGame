from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from blocks import Blocks
from lives import Lives

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("breakout")
screen.tracer(0)

paddle = Paddle((0, -290))
ball = Ball()
scoreboard = Scoreboard()
blocks = Blocks()
lives = Lives()

screen.listen()
screen.onkey(paddle.go_right, "d")
screen.onkey(paddle.go_left, "a")

block_pos = 0
x_val = 250
for i in range(45):
    if i % 15 == 0:
        block_pos = 0
        x_val -= 50
    block_pos += 50
    blocks.level((-400 + block_pos, x_val))


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()

    if ball.distance(paddle) < 60 and ball.ycor() < -260:
        ball.bounce_y()

    if ball.ycor() > 270:
        ball.bounce_y()

    if ball.ycor() < -300:
        lives.lose_life()
        ball.reset_ball()
        paddle.goto(0, -290)

        if lives.life == 0:
            game_is_on = False

    # remove a block if it contacts the ball
    for block in blocks.all_blocks:
        if block.distance(ball) < 30:
            blocks.move_block(block)
            scoreboard.r_point()
            ball.bounce_y()

            if scoreboard.score == 45:
                game_is_on = False
screen.exitonclick()




