import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
cars_list=[]

for _ in range(0,6):
    car = CarManager()
    cars_list.append(car)

scoreboard = Scoreboard()
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")



game_is_on = True
while game_is_on:
    for car_ in cars_list:
        if car_.xcor() < -280:
            car_.restart()
        car_.move_car()
        if player.distance(car_) < 30:
            game_is_on = False
            scoreboard.game_over()
            break
    if player.ycor() > 280:
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        car.car_speed()
        player.restart()
    time.sleep(car.move_speed)
    screen.update()
screen.exitonclick()