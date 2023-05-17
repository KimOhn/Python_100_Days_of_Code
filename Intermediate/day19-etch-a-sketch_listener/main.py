from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500,height = 400)
user_input = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")

color = ["red", "orange", "yellow", "green", "blue", "purple"]
timmys = []

is_race_on = False
if user_input.lower() in color:
    is_race_on = True

y_axis = -150
for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color[i])
    tim.goto(x=-230, y= y_axis)
    y_axis += 50
    timmys.append(tim)

while is_race_on:
    for i in timmys:
        random_dist = random.randint(0,10)
        i.forward(random_dist)
        if i.xcor() > 230:
            is_race_on = False
            winner = list(i.color())[0]
            print(f"the winner is {winner}")

if winner != user_input.lower():
    print("you lost")
else:
    print("you won")




screen.exitonclick()
