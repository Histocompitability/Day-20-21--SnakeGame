from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x=x, y=y)

    def refresh(self):
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        self.goto(x=x, y=y)