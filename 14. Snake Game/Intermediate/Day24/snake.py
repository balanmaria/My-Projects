from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN =270
LEFT=180
RIGHT=0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # create a snake body
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_box = Turtle("square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(position)
        self.segments.append(new_box)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # cumm se misca sarpele:
        # segmentul 3 ii ia locul segmentului 2,
        # segmentul 2 ii ia locul primului segment,
        # iar primul segment inainteaza cu 20 de pasi (lungimea sa)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        #self.segments[0].forward(MOVE_DISTANCE)  # primul segment inainteaza cu 20 de pasi (lungimea sa)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            #self.segments[0].setheading(90)
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            #self.segments[0].setheading(270)
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            #self.segments[0].setheading(180)
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            #self.segments[0].setheading(0)
            self.head.setheading(RIGHT)

    def reset(self):
        #Ca sa nu imi mai ramana sarpele blocat pe ecran, atunci cand pierd un joc
        #il mut in alta parte, mai departe de ecran
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]
