from turtle import Turtle
import turtle
import time
INITIAL_POSITION = [(0, 0), (0, -20), (0, -40)]
STEP_OF_A_SNAKE = 20
FREQUENCY = 0.15


class Snake:

    def __init__(self):
        self.block_bank = []
        self.reset()

    def create_snake(self):
        for position in INITIAL_POSITION:
            self.create_block(position)

    def reset(self):
        for block in self.block_bank:
            block.goto(600, 600)
        self.block_bank.clear()
        self.create_snake()
        self.head = self.block_bank[0]


    def create_block(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.setpos(position)
        self.block_bank.append(t)
    def extend_snake(self):
        self.create_block(self.block_bank[-1].position())

    def move(self):
        turtle.update()
        time.sleep(FREQUENCY)
        for block_number in range(len(self.block_bank) - 1, 0, -1):
            xcord = self.block_bank[block_number - 1].xcor()
            ycord = self.block_bank[block_number - 1].ycor()
            self.block_bank[block_number].goto(xcord, ycord)
        self.head.fd(STEP_OF_A_SNAKE)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
