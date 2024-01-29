from turtle import Turtle
import random

COLORS = ["orange", "yellow", "red", "green", "purple", "blue"]
MOVE_DISTANCE = 5
SPEED_INCREMENT = 5
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle()
            random_y = random.randint(-250, 250)
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for turtle in self.all_cars:
            turtle.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += SPEED_INCREMENT

