from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars_list= []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        cars_list = []
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.car_location()
        self.showturtle()
        self.move_speed=0.1


    def car_location(self):
        #random_x = random.randint(-280, 280)
        random_y = random.randint(-250, 250)
        self.goto(300, random_y)
        #self.goto(0,0)

    def move_car(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x , self.ycor())

    def restart(self):
        self.car_location()

    def car_speed(self):
        self.move_speed *= 0.9
