import time
from turtle import Screen
from a100_days.day_23_turtle_crossing.player import Player
from a100_days.day_23_turtle_crossing.player import FINISH_LINE_Y
from a100_days.day_23_turtle_crossing.car_manager import CarManager
from a100_days.day_23_turtle_crossing.scoreboard import Scoreboard


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.move()

        # Detect if turtle hits the top edge
        if player.ycor() > FINISH_LINE_Y:
            player.win()
            scoreboard.increase_level()
            car_manager.increase_cars_speed()

        # Detect collision with car


        """
        1) Create turtle and move
        2) Create cars and move
        3) Detect if turtle hits the top edge
        4) Detect collision with car
        5) Keep score
        
        """

    screen.exitonclick()


if __name__ == "__main__":
    start()
