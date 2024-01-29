from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.game_restart()
        car_manager.increase_speed()
        scoreboard.level_up()




screen.exitonclick()
