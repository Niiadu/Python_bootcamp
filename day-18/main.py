import turtle
from turtle import Turtle, Screen
import random


timmy = Turtle()
turtle.colormode(255)
timmy.shape("turtle")
angles = [90, 180, 0, 270]
timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(90):
    timmy.color(random_color())
    timmy.left(4)
    # timmy.right(random.choice(angles))
    timmy.circle(80)










screen = Screen()
screen.exitonclick()
