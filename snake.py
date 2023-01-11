from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in POSITIONS:
           self.add_segment(position)

    def add_segment(self, position):
        tim1 = Turtle("square")
        tim1.color("white")
        tim1.penup()
        tim1.goto(position)
        self.segments.append(tim1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segnum - 1].xcor()
            newy = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newx, newy)
        self.head.forward(MOVEDISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
