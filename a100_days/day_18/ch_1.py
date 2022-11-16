from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

screen = Screen()
screen.colormode(255)


def ch1():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def ch2():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def ch3():
    for i in range(3, 11):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.color(color)
        angle = 360 / i
        for _ in range(i):
            timmy.forward(100)
            timmy.right(angle)


def ch4():
    timmy.pensize(15)
    timmy.speed(20)
    angles = (0, 90, 180, 270)
    for _ in range(200):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.color(color)
        timmy.forward(30)
        angle = choice(angles)
        timmy.right(angle)


def ch5():
    timmy.speed(15)
    draw_spirograph(5)


def random_color():
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

ch5()

screen.exitonclick()
