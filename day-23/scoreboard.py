from turtle import Turtle, clear

FONT = ("Courier", 26, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.score = 1
        self.live_score()

    def live_score(self):
        self.write(f"Level: {self.score}", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.live_score()

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=FONT)

