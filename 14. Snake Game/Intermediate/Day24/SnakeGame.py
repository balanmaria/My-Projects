from turtle import Screen
from Intermediate.Day24.ImproveSnakeGame.snake import Snake
from Intermediate.Day24.ImproveSnakeGame.food import Food
from Intermediate.Day24.ImproveSnakeGame.scoreboard import Scoreboard
import time

screen = Screen()  # fereastra care v-a aparea cand rulam programul
screen.setup(width=600, height=600)  # setam dimensiunile ferestrei
screen.bgcolor("black")  # setam culoarea ferestrei sa fie neagra
screen.title("My Snake Game!")  # setam numele ecranului
# turn off the animation of moving
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) #cat de repede se misca sarpele
    snake.move()

    #Detectare mancare
    if snake.head.distance(food) < 15:
        food.refresh()
        #Marire coada cand mananca
        snake.extend()
        scoreboard.increase_score()

    #Lovirea unui perete
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #Mancat coada
    for segemnt in snake.segments[1:]:
        # if segemnt == snake.head:
        #     pass
        if snake.head.distance(segemnt) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()  # fereastra se inchide cand apasam pe ea
