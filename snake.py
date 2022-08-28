from turtle import Turtle

STARTTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.creat()
        self.head = self.segments[0]

    def creat(self):
        for position in STARTTING_POSITION:
            square = Turtle("square")
            square.penup()
            square.color("white")
            square.goto(position)
            self.segments.append(square)

    def segment_add(self,):
        newseg = Turtle("square")
        newseg.penup()
        newseg.color("white")
        newseg.goto(self.segments[-1].pos())
        self.segments.append(newseg)

    def reset(self):
        for seg in self.segments:
            seg.goto(400,400)
        self.segments.clear()
        self.creat()
        self.head = self.segments[0]

    def move(self):

        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)




