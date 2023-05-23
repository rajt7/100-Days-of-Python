from turtle import Turtle, Screen
import random

directions = [0, 90, 180, 270]

tom = Turtle()
screen = Screen()
screen.colormode(255)

tom.pensize(width=7)
tom.speed("fast")

for _ in range(200):
    tom.forward(30)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tom.color(r, g, b)
    tom.setheading(random.choice(directions))

screen.exitonclick()
