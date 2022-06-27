#Extract the color from an image
import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_colors=[]
for color in colors:
    r =color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

#Create a painting
import turtle as t
import random

t.colormode(255)
tim=t.Turtle()
tim.speed(0)
#eliminam liniile
tim.penup()
#ascundem broscuta/sageata
tim.hideturtle()
color_list=[(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()