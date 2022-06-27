import time
from turtle import Screen, Turtle
from Intermediate.Day22.paddle import Paddle
from Intermediate.Day22.ball import Ball
from Intermediate.Day22.scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PongGame")
# turn off the animation of moving
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounds
        ball.ball_hit_the_top_and_the_bottom_wall()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.ball_hit_paddle()

    #Detect when the paddel misses the ball
    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()

    if scoreboard.r_score == 15 or scoreboard.l_score == 15:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
