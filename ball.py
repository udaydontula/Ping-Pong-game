from turtle import Turtle


# import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=.6, stretch_len=.6)
        self.x_move = 10
        self.y_move = 10
        self.refresh()
        self.move_speed = 0.1

    def refresh(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def reverse(self, x, y):
        x_pos = x - 10
        y_pos = y - 6
        self.goto(x_pos, y_pos)

    def bounce(self):
        self.y_move *= - 1

    def bounce_back(self):
        self.x_move *= - 1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.x_move *= - 1
        self.move_speed = 0.1
