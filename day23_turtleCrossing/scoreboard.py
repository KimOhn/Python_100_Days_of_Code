from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg= f"Level: {self.score}", align = "center", font = FONT)

    def inc_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg= "GAME OVER", align = "center", font = FONT)