from turtle import Turtle


MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.game_restart()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def game_restart(self):
        self.goto(0, -280)

