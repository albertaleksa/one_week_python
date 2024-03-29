from turtle import Turtle
from random import choice, randint, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.speed("fastest")
        random_y = randrange(-260, 260, 20)
        self.goto(300, random_y)


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_cars_speed(self):
        self.move_distance += MOVE_INCREMENT

