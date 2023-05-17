from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180
class Paddle(Turtle):
    def __init__(self,x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos,0)

    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)




