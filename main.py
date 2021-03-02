from turtle import Screen, Turtle
import paddle
import ball
import time
import scoreboard


t = Turtle()
screen = Screen()
screen.tracer(0)
screen.setup(width=1000, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()

p1 = paddle.Paddle(480, 0)
p2 = paddle.Paddle(-490, 0)
p3 = Turtle()
b = ball.Ball()
player_1 = scoreboard.Scoreboard(-250, 250)
player_2 = scoreboard.Scoreboard(250, 250)


screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

game_on = True
while game_on:
    b.refresh()
    screen.update()
    time.sleep(b.move_speed)

    if b.ycor() > 290 or b.ycor() < -290:
        b.bounce()

    if b.distance(p1) < 20:
        b.bounce_back()

    if b.distance(p2) < 20:
        b.bounce_back()

    elif b.xcor() > 490:
        b.restart()
        player_1.update()

    elif b.xcor() < -490:
        b.restart()
        player_2.update()

    p3.color("white")
    p3.penup()
    p3.shape("square")
    p3.shapesize(stretch_len=0.1, stretch_wid=1)
    p3.goto(0, 270)

screen.exitonclick()
