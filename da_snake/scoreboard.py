import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x= 0, y= 270)
        self.color("white");
        self.counter_of_a_score = 0

    def write_score(self, score):
        self.clear()
        self.write(f"Score: {score}", False, "Center", ("Arial", 15, "bold"))