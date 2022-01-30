# Make an Etch-A-Sketch App
from turtle import Turtle , Screen
screen = Screen()

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

