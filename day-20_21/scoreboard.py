from turtle import Turtle

FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score_number} High Score {self.high_score}", align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score_number > self.high_score:
            self.high_score = self.score_number
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score_number = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_number += 1
        self.update_scoreboard()


