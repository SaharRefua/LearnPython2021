# import colorgram
# rgb_list = []
# colors = colorgram.extract('hirst-severed-spots-project.jpg', 30)
# print(colors[0].rgb)
# for color in colors:
#     rgb=color.rgb
#     g = rgb.g
#     r = rgb.r
#     b = rgb.b
#     temp= (r,g,b,)
#     rgb_list.append(temp)
#
# print(rgb_list)
#from turtle \
#import Turtle as t
import turtle as t
from turtle import Screen
screen = Screen()
import random
t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
color_list= [ (131, 165, 204), (219, 148, 112), (30, 40, 61), (200, 134, 145), (141, 183, 162), (167, 59, 49), (41, 103, 153), (236, 214, 97), (147, 62, 69), (213, 83, 72), (234, 166, 157), (51, 111, 92), (31, 61, 56), (173, 28, 32), (157, 33, 31), (53, 44, 48), (171, 189, 220), (229, 163, 167), (17, 96, 71), (57, 52, 49), (184, 103, 112), (28, 60, 113), (108, 126, 157), (175, 200, 188), (36, 150, 209), (65, 65, 57)]
tim.penup()
tim.setposition(-400,-350)
#tim.pendown()

def move_one_line_up(number):
    color = random.choice(color_list)

    tim.dot(20, color)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
    #tim.pendown()


for dot_count in range(1, 101):
    color = random.choice(color_list)
    tim.dot(20, color)
    #tim.penup()
    tim.forward(50)
    #tim.pendown()
    if dot_count % 10 == 0:
        print(dot_count)
        move_one_line_up(dot_count )



screen.exitonclick()


#
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = turtle_module.Screen()
# screen.exitonclick()