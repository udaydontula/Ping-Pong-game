from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super(Scoreboard, self).__init__()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.hideturtle()
        self.write(f"Score\n   {0}", align="center", font=("Arial", 12, "normal"))
        self.score = 0

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score\n   {self.score}", align="center", font=("Arial", 12, "normal"))
