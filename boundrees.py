from turtle import Turtle

AGE = 292
SIZE = 3

def boundary():
    boundary = Turtle()
    boundary.color("white")
    boundary.hideturtle()
    boundary.penup()
    boundary.goto(-AGE-4, -AGE+4)
    boundary.pendown()
    boundary.pensize(SIZE)
    for _ in range(4):
        boundary.forward(AGE*2)
        boundary.left(90)
