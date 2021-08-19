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
        ###
        with open("score.txt") as high_score_file:
            self.high_score = high_score_file.read()


    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.write_score()
        with open("score.txt", mode="w") as high_score_file:
            high_score_file.write(str(self.high_score))

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", False, "Center", FONT)
