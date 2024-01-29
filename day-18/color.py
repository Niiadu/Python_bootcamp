# import colorgram
#
# rgb = []
# colors = colorgram.extract('image.jpg', 20 )
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)
import turtle
from turtle import Turtle, Screen
import random
t = Turtle()
color_list = [(235, 232, 227), (230, 233, 239), (239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106)]

turtle.colormode(255)
t.speed("fastest")
t.hideturtle()
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)
number_of_dots = 101

for x in range(1, number_of_dots):
    t.dot(20, random.choice(color_list))
    t.penup()
    t.forward(50)
    if x % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)




screen = Screen()
screen.exitonclick()