###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_lst = rgb_colors[2:len(rgb_colors)-1]

print(color_lst )
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for i in range(1,101):
    new_color = random.choice(color_lst)
    tim.dot(20, new_color)
    tim.forward(30)
    if i % 10 == 0:
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        tim.forward(300)
        tim.right(180)

screen = t.Screen()
screen.exitonclick()

