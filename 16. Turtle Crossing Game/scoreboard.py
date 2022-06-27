from turtle import Turtle
ALIGMENT="center"
FONT=("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over!\nYou have been hit by a car!\nYour level is {self.score}!", align=ALIGMENT, font=FONT)
