from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.load_high_score()
        self.update_scoreboard()


    def update_high_score(self):
        with open("../Desktop/../../../../../../data.txt", "w") as data:
            data.write(str(self.high_score))

    def load_high_score(self):
        with open("/Users/Sahar/Desktop/data.txt") as data:
            temp=data.read()
        self.high_score = int(temp)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
