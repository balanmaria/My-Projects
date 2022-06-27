from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")

# for i in range(1,5):
#     tim.forward(100)
#     tim.right(90)
#
# nr=15
# while nr>0:
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     nr-=1

tim.color("green")
for i in range(1,4):
    tim.forward(100)
    tim.right(120)
tim.color("black")
for i in range(1,5):
    tim.forward(100)
    tim.right(90)
tim.color("red")
for i in range(1,6):
    tim.forward(100)
    tim.right(72)
tim.color("yellow")
for i in range(1,7):
    tim.forward(100)
    tim.right(60)
tim.color("orange")
for i in range(1,8):
    tim.forward(100)
    tim.right(51.42)
tim.color("purple")
for i in range(1,9):
    tim.forward(100)
    tim.right(45)
tim.color("pink")
for i in range(1,10):
    tim.forward(100)
    tim.right(40)
tim.color("blue")
for i in range(1,11):
    tim.forward(100)
    tim.right(36)

def draw_shepe():
    color=["green", "black", "red","yellow", "orange", "purple", "pink", "blue"]
    num_side=[3,4,5,6,7,8,9,10]
    for i in num_side:
        for _ in range(i):
            angle=360/i
            tim.color(color[i-3])
            tim.forward(100)
            tim.right(angle)
draw_shepe()

import random
colors=["green", "black", "red","yellow", "orange", "purple", "pink", "blue"]
def draw_shepe2(num_side):
    angle = 360/num_side
    for i in range(num_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shepe2(shape_side_n)


screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())