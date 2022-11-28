from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_dir = 1
        self.y_dir = 1
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + 10 * self.x_dir
        new_y = self.ycor() + 10 * self.y_dir
        self.goto(new_x, new_y)

    def change_x_dir(self):
        self.x_dir *= -1

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
