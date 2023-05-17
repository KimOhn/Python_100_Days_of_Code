from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            content = int(file.read())
        self.high_score = content
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score =  self.score
        with open("data.txt", mode = "w") as file:
            file.write(f"{self.high_score}")
        self.score =0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align="center")

    # def game_over(self):
    #
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(arg="game over", align="center")

