from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")


class StateTitle(Turtle):

    def __init__(self, title, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.write_title(title, x, y)

    def write_title(self, title, x, y):
        self.goto(x=x, y=y)
        self.write(f"{title}", align=ALIGNMENT, font=FONT)
