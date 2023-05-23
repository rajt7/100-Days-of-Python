from turtle import Turtle, Screen

tom = Turtle()

for _ in range(3):
    tom.forward(15)
    tom.penup()
    tom.forward(10)
    tom.pendown()

screen = Screen()
screen.exitonclick()