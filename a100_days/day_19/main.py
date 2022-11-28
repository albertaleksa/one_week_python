from turtle import Turtle, Screen
from random import randint


def etch_sketch():
    timmy = Turtle()
    screen = Screen()

    def move_forwards():
        timmy.forward(10)

    def move_backwards():
        timmy.back(10)

    def tern_left():
        timmy.left(10)

    def tern_right():
        timmy.right(10)

    def clear_drawing():
        timmy.clear()
        timmy.penup()
        timmy.home()
        timmy.pendown()

    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=tern_left)
    screen.onkey(key="d", fun=tern_right)
    screen.onkey(key="c", fun=clear_drawing)

    screen.exitonclick()


def race():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # timmy = Turtle(shape="turtle")
    # timmy.penup()
    # timmy.goto(x=-230, y=-100)

    turtles = []
    for i in range(6):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.goto(x=-230, y=-70+i*30)
        turtles.append(turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            turtle.forward(randint(1, 10))
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")






    screen.exitonclick()


if __name__ == "__main__":
    # etch_sketch()
    race()
