from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_cars()
        self.speedlimit = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            x_cord = random.randint(-280, 280)
            y_cord = random.randint(-280, 280)
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.shapesize(stretch_wid=1, stretch_len=2)
            tim.color(random.choice(COLORS))
            tim.goto(x_cord, y_cord)
            tim.left(180)
            self.cars.append(tim)


    def drive_cars(self):
        for car in self.cars:
            new_distance = car.xcor() -self.speedlimit
            car.goto(new_distance, car.ycor())

    def inc_speed(self):
        self.speedlimit += MOVE_INCREMENT

