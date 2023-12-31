from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(position=(350, 0))
left_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collision
    if (
        ball.xcor() > right_paddle.left() and
        ball.xcor() < right_paddle.right() and
        right_paddle.bottom() < ball.ycor() < right_paddle.top()
    ):
        ball.bounce_x()

    if (
        ball.xcor() < left_paddle.right() and
        ball.xcor() > left_paddle.left() and
        left_paddle.bottom() < ball.ycor() < left_paddle.top()
    ):
        ball.bounce_x()

    # Reset ball when Right paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.left_add_point()

    # Reset ball when Left paddle misses
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.right_add_point()

screen.exitonclick()
