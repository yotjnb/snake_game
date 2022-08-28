from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial',12,'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt",mode="r") as hscore:
            self.high_score = int(hscore.read())
        self.points = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,275)
        self.board_create()

    def board_create(self):
        self.clear()
        with open("data.txt",mode="r") as hscore:
            hs = hscore.read()
        self.write(f"Score:{self.points} High Score {hs}",False,align=ALIGNMENT,font=FONT)

    def add_points(self):
        self.points += 1
        self.board_create()

    def resets(self):
        if self.points > self.high_score:
            with open("data.txt",mode="w") as hscore:
                hscore.write(str(self.points))
        self.points = 0
        self.board_create()






