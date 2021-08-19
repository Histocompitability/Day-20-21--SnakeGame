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

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "Center", FONT)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "Center", FONT)
