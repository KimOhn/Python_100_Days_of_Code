from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        x_cord = 0
        for i in range(3):
            tim = Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            tim.goto(x_cord,0)
            x_cord -= 20
            self.snakes.append(tim)
    def extend(self):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(self.snakes[-1].position())
        self.snakes.append(tim)
    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)



    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def reset(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snakes()
        self.head = self.snakes[0]