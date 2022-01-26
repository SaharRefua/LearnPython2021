from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 90
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        #self.hideturtle()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        #self.showturtle()

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

    def go_down(self):
        self.backward(MOVE_DISTANCE)
        # new_y = self.ycor() - MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)

    def restart(self):
        self.goto(STARTING_POSITION)