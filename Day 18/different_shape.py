from turtle import Turtle, Screen
from random import randint

tom = Turtle()
screen = Screen()
screen.colormode(255)

for side in range(3, 11):
    angle = 360 / side
    # to use rgb integers we need to set colormode to 255 because rgb range in turtle is 0..colormode
    # where colormode is either set to 1.0 or 255.
    r, g, b = randint(0, 256), randint(0, 256), randint(0, 256)
    while side > 0:
        tom.forward(100)
        tom.right(angle)
        tom.color(r, g, b)
        side -= 1


screen.exitonclick()