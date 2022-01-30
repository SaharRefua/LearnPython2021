# Make a Turtles race
from turtle import Turtle , Screen
import random
screen = Screen()
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
screen.setup(width=500, height=400)
#tim.shape("turtle")
#tim.speed("fastest")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
screen.listen()
turtle_name = "Turtle"
yline = -90
turtles_colors= []
for _ in range(50):
    color = random.choice(colors)
    if len(turtles_colors) < 6:
        if color not in turtles_colors:
            turtles_colors.append(color)
            turtle_name= str(_) + str(color)
            print(turtle_name)
            turtle_name = Turtle(shape="turtle")
            turtle_name.color(color)
            turtle_name.penup()
            turtle_name.goto(x=-230,y=yline)
            yline += 35

screen.exitonclick()

