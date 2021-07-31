import turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.counter_of_a_score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "Center", FONT)

    def write_score(self, score):
        self.clear()
        self.write(f"Score: {score}", False, "Center", FONT)
