from turtle import Screen
import time
from a100_days.day_22_pong.paddle import Paddle
from a100_days.day_22_pong.ball import Ball
from a100_days.day_22_pong.scoreboard import Scoreboard


def start():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong game")
    screen.tracer(0)

    sleep_time = 0.1

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkey(fun=r_paddle.up, key="Up")
    screen.onkey(fun=r_paddle.down, key="Down")

    screen.onkey(fun=l_paddle.up, key="w")
    screen.onkey(fun=l_paddle.down, key="s")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        # Detect when r_paddle misses
        if ball.xcor() > 380:
            scoreboard.increase_l_score()
            ball.reset()

        # Detect when l_paddle misses
        if ball.xcor() < -380:
            scoreboard.increase_r_score()
            ball.reset()


    screen.exitonclick()


if __name__ == "__main__":
    start()

"""
1) Field (Create the screen)
2) Player 1 (Create and move a paddle)
3) Player 2 (Create another paddle)
4) Ball (Create a Ball and make it move)
5) Detect collision with wall and bounce
6) Detect collision with paddle
7) Detect when paddle misses
8) Keep score
"""