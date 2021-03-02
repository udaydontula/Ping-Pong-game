from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super(Paddle, self).__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=0.3, stretch_wid=2.5)
        self.goto(-490, 0)

    def up(self):
        new_pos = self.ycor() + 20
        self.goto(x=490, y=new_pos)

    def down(self):
        new_pos = self.ycor() - 20
        self.goto(x=490, y=new_pos)
