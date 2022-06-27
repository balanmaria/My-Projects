from turtle import Turtle, Screen

tim= Turtle()


def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterClockwise():
    tim.left(10)
    # new_heading=tim.heading() + 10
    # tim.setheading(new_heading)

def move_Clockwise():
    tim.right(10)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    #tim.setposition(0.0, 0.0)
    tim.home()
    tim.pendown()


screen= Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterClockwise)
screen.onkey(key="d", fun=move_Clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()