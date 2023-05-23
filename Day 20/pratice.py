from turtle import Turtle, Screen

HEADING = {'up': 90, 'down': 270, 'left': 180, 'right': 0}
tom = Turtle()
tom.forward(200)
tom.setheading(HEADING['right'])

screen = Screen()
screen.exitonclick()
