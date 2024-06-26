from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.score_update()

    def r_point(self):
        self.r_score += 1
        self.score_update()

    def winner(self):
        if self.l_score > 2:
            self.goto(0, 0)
            self.write("left wins", align="center", font=("Courier", 80, "normal"))
        elif self.r_score > 2:
            self.goto(0, 0)
            self.write("right wins", align="center", font=("Courier", 80, "normal"))
