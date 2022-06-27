import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car= CarManager()

scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    #Detect collision with car
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if player.ycor() == 280:
        scoreboard.increase_score()
        player.go_to_start()
        car.increase_speed_of_the_car()


screen.exitonclick()