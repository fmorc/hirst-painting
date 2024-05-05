# import colorgram
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))
#
# print(color_list)
import random
from turtle import Turtle, Screen

color_list = [(198, 165, 116), (144, 79, 55), (221, 201, 138), (58, 93, 121), (167, 153, 48), (132, 34, 23),
              (137, 162, 181), (69, 40, 34), (51, 117, 87), (195, 93, 75), (146, 178, 150), (18, 93, 72),
              (231, 176, 165), (162, 143, 158), (35, 60, 75), (105, 73, 77), (180, 204, 177), (148, 19, 23),
              (83, 147, 127), (70, 37, 40), (18, 70, 60), (27, 82, 88), (40, 66, 89), (190, 86, 89), (68, 64, 58),
              (223, 176, 180)]

screen = Screen()
screen.colormode(255)
width = screen.window_width()
height = screen.window_height()

turtle = Turtle()
turtle.penup()
turtle.speed(0)
turtle.hideturtle()

for j in range(10):
    turtle.goto(width / 2 * -1 + 200, height / 2 * -1 + ((j+1) * 50))
    for _ in range(10):
        turtle.fillcolor(random.choice(color_list))
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.forward(50)
screen.exitonclick()





