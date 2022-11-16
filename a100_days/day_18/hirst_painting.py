import colorgram
from turtle import Turtle, Screen
from random import choice

X0_POSITION = -200
Y0_POSITION = -200
TURTLE_SPEED = "fastest"
DOT_COUNTS = 10
DOT_SIZE = 20
DOT_GAP = 50


def get_color(colors):
    while True:
        color = choice(colors).rgb
        if color.r < 240 and color.g < 240 and color.b < 240:
            break
    return color


def draw_line(turtle, colors, dot_counts, dot_size, gap):
    for _ in range(dot_counts):
        # turtle.color(get_color(colors))
        turtle.pendown()
        turtle.dot(dot_size, get_color(colors))
        turtle.penup()
        turtle.forward(gap)


def draw_square(turtle, colors, dot_counts, dot_size, gap):
    for _ in range(dot_counts):
        draw_line(turtle, colors, dot_counts=dot_counts, dot_size=dot_size, gap=gap)
        turtle.goto(X0_POSITION, turtle.ycor() + gap)


def start():
    timmy = Turtle()
    screen = Screen()
    screen.colormode(255)
    timmy.speed(TURTLE_SPEED)
    timmy.hideturtle()

    timmy.penup()
    timmy.goto(X0_POSITION, Y0_POSITION)
    timmy.pendown()

    colors = colorgram.extract('image.jpeg', 30)

    draw_square(timmy, colors, dot_counts=DOT_COUNTS, dot_size=DOT_SIZE, gap=DOT_GAP)

    screen.exitonclick()


if __name__ == "__main__":
    start()
