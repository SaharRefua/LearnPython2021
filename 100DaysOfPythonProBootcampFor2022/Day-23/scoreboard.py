from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT="center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER !", align=ALIGNMENT, font=FONT)