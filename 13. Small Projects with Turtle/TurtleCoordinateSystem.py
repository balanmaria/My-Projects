import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

#setam dimensiunea screen-ului
screen.setup(width=500, height=400)
#create the pop-up
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-70, -40, -10, 20, 50, 80]
all_turtle=[]

for nr in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[nr])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=position[nr])
    all_turtle.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!\nYour bet was {user_bet}!")
            is_race_on=False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
