from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.speed("fastest")

for _ in range(36):
    tom.circle(50)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    tom.color(r, g, b)
    tom.left(10)

screen.exitonclick()
