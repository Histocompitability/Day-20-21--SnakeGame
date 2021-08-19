import turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.score = 0
        self.high_score = 0

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", False, "Center", FONT)
