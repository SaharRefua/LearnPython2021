# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

#from turtle import Turtle , Screen
#from random \
import random
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("red")
# #
# for _ in range (4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
#
# for _ in range(8):
#     for _ in range(8):
#         my_turtle.forward(10)
#         my_turtle.penup()
#         my_turtle.forward(10)
#         my_turtle.pendown()
#     my_turtle.right(45)
# lines = 3
# for _ in range(7):
#     # color = { random.randint(0, 10), random.randint(0, 10), random.randint(0, 10) }
#     # print(type(color))
#     # my_turtle.pencolor(color)
#     for _ in range(lines):
#         my_turtle.forward(100)
#         my_turtle.right(360/lines)
#     lines+=1
# screen = Screen()
# screen.exitonclick()



import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed("fastest")
########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0,90,280,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# def do_step(dir):#, dir):
#     tim.setheading(dir)
#     tim.forward(30)
#     tim.color(random_color())
#
# for _ in range (50):
#     do_step(random.choice(direction))     #(random.choice(colours), random.choice(direction))
#
#
#



#tim.circle(120, 180)
for angle in range(360):
    #tim.setheading(angle)
    tim.circle(120 )
    tim.color(random_color())
    print(tim.position())
    angle =+ 5
    tim.left(angle)
    tim.backward(angle)


# import turtle as t
# import random
#
# tim = t.Turtle()
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# ########### Challenge 5 - Spirograph ########
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


